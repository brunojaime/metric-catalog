from server import mcp
from services.catalog_service import MetricCatalogService  

catalog_service : MetricCatalogService = None

@mcp.tool()
def get_metric_catalog() -> str:
    """Returns the metric catalog as a formatted string."""
    return catalog_service.get_readable_catalog()


@mcp.tool()
def get_all_metric_metadata_fields() -> list[str]:
    """
    Returns the list of available metadata fields found in the metric catalog.
    """
    try:
        return catalog_service.get_metadata_fields()
    except ValueError as e:
        return [f"Error: {str(e)}"]
    
@mcp.tool()
def get_metric_catalog_fields(fields: list[str]) -> list[dict]:
    """
    Returns all metrics from the metric catalog, but only with the selected metadata fields.
    """
    try:
        return catalog_service.get_catalog_selected_fields(fields)
    except ValueError as e:
        return [f"Error: {str(e)}"]

@mcp.tool()
def get_metric_by_name(name: str, attributes: list[str] ) -> list[dict]:
    """
    Returns a metric by its name, optionally with selected attributes from the catalog.
    """
    try:
        return catalog_service.get_metric(name, attributes)
    except ValueError as e:
        return {"error": str(e)}