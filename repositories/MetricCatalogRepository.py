from abc import ABC, abstractmethod
from typing import List, Dict
from typing import List, Dict, Optional

class MetricCatalogRepository(ABC):
    @abstractmethod
    def get_catalog(self) -> List[Dict[str, str]]:
        """Returns a list of metrics."""
        pass

    def get_metric_by_name(self, name: str) -> Optional[Dict[str, str]]:
        """Returns a single metric by name or None if not found."""
        pass