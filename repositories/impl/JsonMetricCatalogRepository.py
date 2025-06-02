import json
from typing import List, Dict
from repositories.MetricCatalogRepository import MetricCatalogRepository
import os

class JSONMetricCatalogRepository(MetricCatalogRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path

    @staticmethod
    def from_env() -> 'JSONMetricCatalogRepository':
        path = os.getenv("CATALOG_PATH")
        if not path:
            raise ValueError("CATALOG_PATH is required for JSON source")
        return JSONMetricCatalogRepository(path)

    def get_catalog(self) -> List[Dict[str, str]]:
        with open(self.file_path, "r") as f:
            return json.load(f)
