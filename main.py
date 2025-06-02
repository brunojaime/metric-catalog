from dotenv import load_dotenv
load_dotenv()
import os
from registry.catalog_registry import CatalogRegistry
from services.catalog_service import MetricCatalogService
import tools
from server import mcp


def setup():
    repo = CatalogRegistry.resolve_repository()
    tools.catalog_service = MetricCatalogService(repo)
    metric_name_field = os.getenv("METRIC_NAME_FIELD")
    if not metric_name_field:
            raise ValueError("METRIC_NAME_FIELD environment variable is not set")
    tools.catalog_service.set_metric_name_field(metric_name_field)

if __name__ == "__main__":
    setup()
    mcp.run(transport="sse")