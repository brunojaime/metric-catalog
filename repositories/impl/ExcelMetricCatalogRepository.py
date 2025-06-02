import os
import pandas as pd 
from typing import List, Dict
from repositories.MetricCatalogRepository import MetricCatalogRepository

class ExcelMetricCatalogRepository(MetricCatalogRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path

    @staticmethod
    def from_env() -> 'ExcelMetricCatalogRepository':
        path = os.getenv("CATALOG_PATH")
        if not path:
            raise ValueError("CATALOG_PATH is required for Excel source")
        return ExcelMetricCatalogRepository(path)

    def get_catalog(self) -> List[Dict[str, str]]:
        df = pd.read_excel(self.file_path)
        return df.fillna("").to_dict(orient="records")
    
    def get_metric_by_name(self, name):
        return super().get_metric_by_name(name)
