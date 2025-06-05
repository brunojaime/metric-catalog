from abc import ABC, abstractmethod
from typing import List, Dict, Optional


class INormalizedMetricCatalogRepository(ABC):
    @abstractmethod
    def save_catalog(self, catalog: List[Dict[str, str]]) -> None:
        """Persists the normalized catalog to storage."""
        pass

    @abstractmethod
    def get_catalog(self) -> List[Dict[str, str]]:
        """Returns the list of normalized metrics."""
        pass

    @abstractmethod
    def get_attribute_by_name(self, field: str, name: str) -> Optional[Dict[str, str]]:
        """Returns a metric where `field` (e.g., 'name') matches `name` (case-insensitive, normalized)."""
        pass
