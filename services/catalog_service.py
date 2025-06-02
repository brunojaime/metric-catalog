from repositories.MetricCatalogRepository import MetricCatalogRepository
from typing import List, Dict

class MetricCatalogService:
    def __init__(self, repo: MetricCatalogRepository):
        self.repo = repo

    def get_readable_catalog(self) -> str:
        metrics: List[Dict[str, str]] = self.repo.get_catalog()
        return "\n".join(f"{m['name']} - {m['description']}" for m in metrics)
