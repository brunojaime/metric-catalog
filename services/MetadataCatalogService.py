
from typing import List, Dict, Optional
from repositories.AttributeMetadataRepository.IAttributeMetadataRepository import IAttributeMetadataRepository

from repositories.NormalizedCatalogRepository import INormalizedMetricCatalogRepository



class MetadataCatalogService:
    def __init__(self, repo_metadata: IAttributeMetadataRepository,repo_normalized_catalog: INormalizedMetricCatalogRepository):
        self.repo_metadata = repo_metadata
        self.repo_normalized = repo_normalized_catalog

    def get_metadata_fields(self) -> list[str]:
        catalog = self.repo_metadata.get_all()
        if not catalog:
            raise ValueError("Metadata catalog is empty")

        # Suponiendo que cada dict tiene una key "name"
        fields = [item["name"] for item in catalog if "name" in item]
        return sorted(fields)

    def get_metadata_for_catalog_fields(self, field : str) -> Optional[Dict]:
        normalized_field = self.repo_normalized.get_attribute_by_name(field.strip().lower())
           

        catalog = self.repo_metadata.get_all()
        if not catalog:
            raise ValueError("Metadata catalog is empty")

        for item in catalog:
            if item.get("attribute_id") == normalized_field:
                return item

        return None
    

if __name__ == "__main__":
    from repositories.NormalizedCatalogRepository.impl.JSONNormalizedMetricCatalogRepository import JSONNormalizedMetricCatalogRepository
    from repositories.AttributeMetadataRepository.impl.JsonAttributeMetadataRepository import JSONAttributeMetadataRepository
    repo_metadata = JSONAttributeMetadataRepository("data/metadata_catalog/meta_data2.json")
    repo_normalized = JSONNormalizedMetricCatalogRepository("data/metric_catalog.json")

    service = MetadataCatalogService(repo_metadata, repo_normalized)
    get_metadata_fields = service.get_metadata_for_catalog_fields("Last Updated")
    print(get_metadata_fields)