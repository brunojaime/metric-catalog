import csv
from typing import List, Dict
from repositories.MetricCatalogRepository import MetricCatalogRepository
import os

class CSVMetricCatalogRepository(MetricCatalogRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path

    @staticmethod
    def from_env() -> 'CSVMetricCatalogRepository':
        path = os.getenv("CATALOG_PATH")
        if not path:
            raise ValueError("CATALOG_PATH is required for CSV source")
        return CSVMetricCatalogRepository(path)

    def get_catalog(self) -> List[Dict[str, str]]:
        with open(self.file_path, newline='') as f:
            return list(csv.DictReader(f))