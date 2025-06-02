from server import mcp
from services.catalog_service import MetricCatalogService  

catalog_service : MetricCatalogService = None

@mcp.tool()
def get_metric_catalog() -> str:
    """Returns the metric catalog as a formatted string."""
    return catalog_service.get_readable_catalog()


@mcp.tool()
def get_metric_metadata_fields() -> list[str]:
    """
    Returns the list of available metadata fields found in the catalog.
    """
    return catalog_service.get_metadata_fields()