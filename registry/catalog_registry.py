import os
from repositories.MetricCatalogRepository import MetricCatalogRepository
from repositories.impl.JsonMetricCatalogRepository import JSONMetricCatalogRepository
from repositories.impl.CSVMetricCatalogRepository import CSVMetricCatalogRepository
from repositories.impl.ExcelMetricCatalogRepository import ExcelMetricCatalogRepository
from dotenv import load_dotenv

load_dotenv()
class CatalogRegistry:
    @staticmethod
    def resolve_repository() -> MetricCatalogRepository:
        source = os.getenv("CATALOG_SOURCE")
        if not source:
            raise ValueError("Missing required env var: CATALOG_SOURCE")

        source = source.lower()

        if source == "json":
            return JSONMetricCatalogRepository.from_env()
        elif source == "csv":
            return CSVMetricCatalogRepository.from_env()
        elif source == "xlsx":
            return ExcelMetricCatalogRepository.from_env()

        else:
            raise ValueError(f"Unsupported CATALOG_SOURCE: {source}")