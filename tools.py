from server import mcp  

catalog_service= None

@mcp.tool()
def get_metric_catalog() -> str:
    """Returns the metric catalog as a formatted string."""
    return catalog_service.get_readable_catalog()
