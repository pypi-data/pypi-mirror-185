from abc import ABCMeta
from abc import abstractmethod
from typing import Dict

from katatachi.content import ContentStore

from .column_render import ModViewColumnRender


class ModViewColumn(metaclass=ABCMeta):
    @abstractmethod
    def render(
        self, document: Dict, content_store: ContentStore
    ) -> ModViewColumnRender:
        pass

    @abstractmethod
    def has_callback(self) -> bool:
        pass

    @abstractmethod
    def callback_id(self) -> str:
        pass

    @abstractmethod
    def callback(self, document: Dict, content_store: ContentStore):
        pass


class NonCallbackModViewColumn(ModViewColumn):
    @abstractmethod
    def render(
        self, document: Dict, content_store: ContentStore
    ) -> ModViewColumnRender:
        pass

    def has_callback(self) -> bool:
        return False

    def callback_id(self) -> str:
        return ""

    def callback(self, document: Dict, content_store: ContentStore):
        pass
