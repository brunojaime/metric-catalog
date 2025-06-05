from server import mcp
from services.CatalogService import MetricCatalogService  
from services.MetadataCatalogService import MetadataCatalogService
from services.catalog_introspection_service import CatalogIntrospectionService


catalog_service : MetricCatalogService = None
metadata_service: MetadataCatalogService = None
catalog_introspection_service: CatalogIntrospectionService = CatalogIntrospectionService(catalog_service, metadata_service)

@mcp.tool()
def get_catalog() -> list[dict]:
    """
    Returns the entire metric catalog as a list of dictionaries.
    Each dictionary represents a metric with its attributes.
    """
    try:
        return catalog_service.get_catalog()
    except ValueError as e:
        return [f"Error: {str(e)}"]



@mcp.tool()
def get_metric_catalog_fields() -> list[str]:  
    """
    Returns the list of available fields in the metric catalog.
    This includes all fields that can be used to filter or select metrics.
    """
    try:
        return catalog_service.get_attribute_fields()
    except ValueError as e:
        return [f"Error: {str(e)}"]

def get_attribute_metadata(attribute_name: str) -> dict:
    """
    Returns metadata details about a specific attribute (i.e., a field in the catalog), 
    such as its description, data type, examples, and intended purpose.

    Note: This method expects the name of a **field or attribute**, not a metric name.
    It's ideal to use this when additional context about catalog fields is needed.
    """

    try: return metadata_service.get_metadata_for_catalog_fields(attribute_name)
    except ValueError as e:
        return {"Error": str(e)}


@mcp.tool()
def get_metadata_catalog() -> str:
    """Returns the metadata catalog as a formatted string."""
    return metadata_service.get_metadata_fields()



@mcp.tool()
def get_metric_catalog_fields(fields: list[str]) -> list[dict]:
    """
    Returns all metrics from the metric catalog, but only with the selected metadata fields.
    """
    try:
        return catalog_service.get_catalog_selected_fields(fields)
    except ValueError as e:
        return [f"Error: {str(e)}"]
'''


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
def get_metric_by_name(name: str, attributes: list[str] ) -> list[dict]:
    """
    Returns a metric by its name, optionally with selected attributes from the catalog.
    """
    try:
        return catalog_service.get_metric(name, attributes)
    except ValueError as e:
        return {"error": str(e)}
    


@mcp.tool()
def get_combined_attribute_metadata() -> dict:
    """
    Returns enriched metadata for the attributes present in the catalog.
    """
    return catalog_introspection_service.get_combined_attribute_metadata()

'''   
