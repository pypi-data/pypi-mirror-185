from typing import Dict, List, Optional

from katatachi.content import ContentStore
from katatachi.interface.mod_view import ModViewColumn
from katatachi.interface.mod_view import ModViewColumnRender
from katatachi.mod_view.mod_view_query import ModViewQuery

DEFAULT_RENDER_LIMIT = 50


class ModViewRenderer(object):
    def __init__(self, content_store: ContentStore):
        self.content_store = content_store
        self.callbacks = {}  # type: Dict[str, ModViewColumn]

    def render_as_dict(
        self, mod_view_query: ModViewQuery
    ) -> List[Dict[str, Optional[Dict]]]:
        # register callbacks
        for projection in mod_view_query.projections:
            column = projection.column
            if column.has_callback():
                self.callbacks[column.callback_id()] = column

        # do the query
        documents = self.content_store.query(
            q=mod_view_query.query, limit=DEFAULT_RENDER_LIMIT, sort=mod_view_query.sort
        )

        # render rows
        rows = []
        for d in documents:
            row_renders = {}
            for named_columns in mod_view_query.projections:
                column_name, column = named_columns.name, named_columns.column
                row_renders[column_name] = self._render_to_dict(
                    column.render(d, self.content_store)
                )
                if column.has_callback():
                    row_renders[column_name]["callback_id"] = column.callback_id()
            rows.append({"renders": row_renders, "raw_document": d})

        return rows

    def callback(self, callback_id: str, document: Dict):
        if callback_id in self.callbacks:
            self.callbacks[callback_id].callback(document, self.content_store)
        # TODO: error here

    @staticmethod
    def _render_to_dict(render: ModViewColumnRender) -> Dict:
        return {"type": render.render_type(), "data": render.render_data()}
