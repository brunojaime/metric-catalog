from repositories.MetricCatalogRepository import MetricCatalogRepository
from typing import List, Dict
import inflect

p = inflect.engine()

class MetricCatalogService:
    def __init__(self, repo: MetricCatalogRepository):
        self.repo = repo
        self._metric_name_field = None

    def set_metric_name_field(self, field_name: str):
        self._metric_name_field = field_name.strip()

    def get_readable_catalog(self) -> str:
        metrics: List[Dict[str, str]] = self.repo.get_catalog()
        return "\n".join(f"{m['name']} - {m['description']}" for m in metrics)
    

    def get_metadata_fields(self) -> list[str]:
        catalog = self.repo.get_catalog()
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

        available_fields = set(catalog[0].keys())  # base it on first row
        missing = [f for f in fields if f not in available_fields]

        if missing:
            raise ValueError(f"Unknown fields: {', '.join(missing)}")

        return [{f: metric.get(f) for f in fields} for metric in catalog]
    
    def normalize(self, value: str) -> str:
        return p.singular_noun(value.strip().lower()) or value.strip().lower()
    
    
    def get_metric(self, entity: str, attributes: list[str] | None = None) -> dict:
        normalized = self.normalize(entity)
        metric = self.repo.get_metric_by_name(self._metric_name_field, normalized)

        if not metric:
            raise ValueError(f"Metric '{entity}' not found.")

        if attributes:
            return {attr: metric.get(attr) for attr in attributes}
        return metric