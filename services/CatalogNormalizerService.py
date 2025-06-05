from typing import List,Dict
from repositories.MetricCatalogRepository import IMetricCatalogRepository
from repositories.NormalizedCatalogRepository import INormalizedMetricCatalogRepository
import re


class CatalogNormalizerService:
    def __init__(self, client_repo: IMetricCatalogRepository, repo_normalized_catalog: INormalizedMetricCatalogRepository):
        self.repo_normalized_catalog = repo_normalized_catalog
        self.client_repo = client_repo

    def get_attribute_fields(self) -> list[str]:
        catalog = self.client_repo.get_catalog()
        if not catalog:
            raise ValueError("Metric catalog is empty")

        fields = set()
        for item in catalog:
            fields.update(item.keys())

        return sorted(fields)

    def generate_attribute_id(self,display_name: str) -> str:
        return re.sub(r"\s+", "_", display_name.strip().lower())

    def get_display_to_id_map(self, catalog_fields: List[str]) -> Dict[str, str]:
        result = {}
        for display_name in catalog_fields:
            key = display_name.strip().lower()
            attr_id = self.generate_attribute_id(display_name)
            result[key] = attr_id
        return result
    def save_normalized_catalog(self, normalized_catalog: List[Dict[str, str]]) -> None:
        self.repo_normalized_catalog.save_catalog(normalized_catalog)

        
if __name__ == "__main__":
    # Example usage
    from repositories.MetricCatalogRepository.impl.JSONMetricCatalogRepository import JSONMetricCatalogRepository
    from repositories.NormalizedCatalogRepository.impl.JSONNormalizedMetricCatalogRepository import JSONNormalizedMetricCatalogRepository

    client_repo = JSONMetricCatalogRepository("data/metrics.json")
    normalized_repo = JSONNormalizedMetricCatalogRepository("data/metric_catalog.json")

    service = CatalogNormalizerService(client_repo, normalized_repo)
    
    noramalized_catalog = service.get_display_to_id_map(service.get_attribute_fields())
    service.save_normalized_catalog(noramalized_catalog)
    print("Normalized catalog generated successfully.")