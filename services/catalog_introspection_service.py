from services.CatalogService import MetricCatalogService
from services.MetadataCatalogService import MetadataCatalogService

class CatalogIntrospectionService:
    def __init__(self, metric_service: MetricCatalogService, metadata_service: MetadataCatalogService):
        self.metric_service = metric_service
        self.metadata_service = metadata_service

    
    def get_combined_attribute_metadata(self) -> dict:
        catalog_fields = set(self.metric_service.get_attribute_fields())
        full_metadata = self.metadata_service.get_metadata_fields()

        result = {}

        for metadata_key, metadata_value in full_metadata.items():
            if metadata_key in catalog_fields:
                result[metadata_key] = metadata_value

        return result
