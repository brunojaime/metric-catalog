from factories import attribute_metadata_factory
from repositories.MetricCatalogRepository import IMetricCatalogRepository
from repositories.AttributeMetadataRepository import IAttributeMetadataRepository
from typing import List, Dict
import inflect
from repositories.NormalizedCatalogRepository import INormalizedMetricCatalogRepository

p = inflect.engine()

class MetricCatalogService:
    def __init__(self, repo_catalog: IMetricCatalogRepository,repo_attributes: IAttributeMetadataRepository):
        self.repo_catalog = repo_catalog
        self._metric_name_field = None
        self.repo_attributes =  repo_attributes

    
    

    def get_attribute_fields(self) -> list[str]:
        catalog = self.repo_catalog.get_catalog()
        if not catalog:
            raise ValueError("Metric catalog is empty")

        fields = set()
        for item in catalog:
            fields.update(item.keys())

        return sorted(fields)

    def get_catalog_selected_fields(self, fields: list[str]) -> list[dict]:
        catalog = self.repo.get_catalog()
        if not catalog:
            raise ValueError("The metric catalog is empty.")

        available_fields = set(catalog[0].keys())  
        missing = [f for f in fields if f not in available_fields]

        if missing:
            raise ValueError(f"Unknown fields: {', '.join(missing)}")

        return [{f: metric.get(f) for f in fields} for metric in catalog]
    
    



    def normalize(self, value: str) -> str:
        return p.singular_noun(value.strip().lower()) or value.strip().lower()
    
    
    def set_metric_name_field(self, field_name: str):
        self._metric_name_field = field_name.strip()



    def get_metric(self, entity: str, attributes: list[str] | None = None) -> dict:
        normalized = self.normalize(entity)
        metric = self.repo.get_metric_by_name(self._metric_name_field, normalized)

        if not metric:
            raise ValueError(f"Metric '{entity}' not found.")

        if attributes:
            return {attr: metric.get(attr) for attr in attributes}
        return metric
    
    def save_attribute_metadata(self) -> None:
        metadata = self.get_attribute_fields()
        if not metadata:
            raise ValueError("Metadata cannot be empty.")
        metadata_attributes = attribute_metadata_factory(metadata)
        self.repo_attributes.save_attribute_metadata(metadata)