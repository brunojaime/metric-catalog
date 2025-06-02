import json
from typing import List, Dict,Optional
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
    
    
    def get_metric_by_name(self, field: str, value: str) -> Optional[Dict[str, str]]:
        value_normalized = value.strip().lower()
        with open(self.file_path, "r") as f:
            catalog = json.load(f)

        for metric in catalog:
            field_value = metric.get(field, "")
            if isinstance(field_value, str) and field_value.strip().lower() == value_normalized:
                return metric

        return None