import json
import os
from typing import List, Dict, Optional
from repositories.NormalizedCatalogRepository.INormalizedMetricCatalogRepository import INormalizedMetricCatalogRepository
import inflect

p = inflect.engine()


class JSONNormalizedMetricCatalogRepository(INormalizedMetricCatalogRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._cache: Optional[List[Dict[str, str]]] = None

    def save_catalog(self, catalog: List[Dict[str, str]]) -> None:
        with open(self.file_path, "w") as f:
            json.dump(catalog, f, indent=2)
        self._cache = catalog

    def get_catalog(self) -> List[Dict[str, str]]:
        if self._cache is not None:
            return self._cache
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as f:
            self._cache = json.load(f)
        return self._cache

    def get_attribute_by_name(self, field: str) -> Optional[Dict[str, str]]:
        normalized_attribute = self.get_catalog()[field]
        if not normalized_attribute:
            return None
        return normalized_attribute

    def _normalize(self, value: str) -> str:
        value = value.strip().lower()
        return p.singular_noun(value) or value
