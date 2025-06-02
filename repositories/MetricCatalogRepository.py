from abc import ABC, abstractmethod
from typing import List, Dict

class MetricCatalogRepository(ABC):
    @abstractmethod
    def get_catalog(self) -> List[Dict[str, str]]:
        """Returns a list of metrics with name and description."""
        pass
