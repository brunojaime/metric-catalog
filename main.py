from dotenv import load_dotenv

from registry.metadata_catalog_registry import MetadataCatalogRegistry
from repositories.NormalizedCatalogRepository.impl.JSONNormalizedMetricCatalogRepository import JSONNormalizedMetricCatalogRepository
from services.MetadataCatalogService import MetadataCatalogService
load_dotenv()
import os
from registry.catalog_registry import CatalogRegistry
from services.CatalogService import MetricCatalogService
import tools
from server import mcp


def setup():
    catalog_repo = CatalogRegistry.resolve_repository()
    metadata_repo = MetadataCatalogRegistry.resolve_repository()
    normalized_catalog_repo = JSONNormalizedMetricCatalogRepository("data/metric_catalog.json")
    tools.catalog_service = MetricCatalogService(catalog_repo,metadata_repo)
    tools.metadata_service = MetadataCatalogService(metadata_repo,normalized_catalog_repo)
    metric_name_field = os.getenv("METRIC_NAME_FIELD")
    if not metric_name_field:
            raise ValueError("METRIC_NAME_FIELD environment variable is not set")
    tools.catalog_service.set_metric_name_field(metric_name_field)

if __name__ == "__main__":
    setup()
    mcp.run(transport="sse")