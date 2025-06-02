from dotenv import load_dotenv
load_dotenv()

from registry.catalog_registry import CatalogRegistry
from services.catalog_service import MetricCatalogService
import tools
from server import mcp

def setup():
    repo = CatalogRegistry.resolve_repository()
    tools.catalog_service = MetricCatalogService(repo)
                
if __name__ == "__main__":
    setup()
    mcp.run(transport="sse")