import logging
import time
import uuid
from typing import Callable, Dict, Optional, Tuple
from sentry_sdk import capture_exception
from katatachi.interface.worker import Worker
from .work_context import WorkContextFactory
from .worker_cache import WorkerCache
from .worker_config_store import WorkerConfigStore
from .worker_run_store import WorkerRunStore, WorkerRunMetadata, WorkerRunState

logger = logging.getLogger(__name__)


class WorkFactory(object):
    def __init__(
        self,
        work_context_factory: WorkContextFactory,
        worker_cache: WorkerCache,
        worker_config_store: WorkerConfigStore,
        worker_run_store: WorkerRunStore,
        sentry_enabled: bool,
    ):
        self.work_context_factory = work_context_factory
        self.worker_cache = worker_cache
        self.worker_config_store = worker_config_store
        self.worker_run_store = worker_run_store
        self.sentry_enabled = sentry_enabled

    def get_work_func(
        self, module_name: str, args: Dict
    ) -> Optional[Tuple[Callable, str]]:
        status, worker_or_message = self.worker_cache.load(module_name, args)
        if not status:
            logger.error(
                "Fails to load worker",
                extra={
                    "module_name": module_name,
                    "args": args,
                    "message": worker_or_message,
                },
            )
            return None

        worker = worker_or_message  # type: Worker
        worker_id = worker.get_id()
        run_id = str(uuid.uuid4())

        self.worker_run_store.add(
            worker_run_metadata=WorkerRunMetadata(
                module_name=module_name,
                args=args,
                run_id=run_id,
            ),
            initial_state=WorkerRunState.Running
        )

        error_resiliency = self.worker_config_store.get_error_resiliency(worker_id)
        work_context = self.work_context_factory.build(worker_id, run_id)

        worker.pre_work(work_context)

        def work_func():
            try:
                worker.work(work_context)
                # always reset error count
                ok, err = self.worker_config_store.reset_error_count(worker_id)
                if not ok:
                    logger.error(
                        "Fails to reset error count",
                        extra={"worker_id": worker_id, "reason": err},
                    )
                self.worker_run_store.update_state(worker_id, run_id, WorkerRunState.Succeeded)
            except Exception as e:
                report_ex = True
                if error_resiliency > 0:
                    ok, error_count, err = self.worker_config_store.get_error_count(
                        worker_id
                    )
                    if not ok:
                        logger.error(
                            "Fails to get error count",
                            extra={"worker_id": worker_id, "reason": err},
                        )
                    if error_count < error_resiliency:
                        # only not to report exception when error resiliency is set and error count is below resiliency
                        report_ex = False

                if report_ex:
                    if self.sentry_enabled:
                        capture_exception(e)
                    else:
                        logger.exception(
                            "Fails to execute work",
                            extra={"worker_id": worker_id, "reason": e},
                        )
                else:
                    logger.info(
                        "Not reporting exception because of error resiliency",
                        extra={"worker_id": worker_id, "reason": e},
                    )

                if error_resiliency > 0:
                    # only to touch error count if error resiliency is set
                    ok, err = self.worker_config_store.increment_error_count(worker_id)
                    if not ok:
                        logger.error(
                            "Fails to increment error count",
                            extra={"worker_id": worker_id, "reason": err},
                        )

                self.worker_run_store.update_state(worker_id, run_id, WorkerRunState.Failed)

            self.worker_config_store.set_last_executed_seconds(
                worker_id, int(time.time())
            )

        return work_func, worker_id
