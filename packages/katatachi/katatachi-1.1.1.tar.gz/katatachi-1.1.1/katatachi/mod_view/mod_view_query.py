from dataclasses import dataclass
from typing import Dict, List, Optional

from katatachi.interface.mod_view import ModViewColumn


@dataclass
class NamedModViewColumn:
    name: str
    column: ModViewColumn

    def to_dict(self):
        return {
            "name": self.name,
        }


@dataclass
class ModViewQuery:
    query: Dict
    projections: List[NamedModViewColumn]
    sort: Optional[Dict] = None

    def to_dict(self):
        d = {
            "q": self.query,
            "projections": list(map(lambda p: p.to_dict(), self.projections)),
        }
        if self.sort:
            d["sort"] = self.sort
        return d
