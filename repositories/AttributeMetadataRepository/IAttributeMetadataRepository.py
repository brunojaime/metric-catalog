from abc import ABC, abstractmethod
from typing import Dict, Optional, List
from models.AttributeMetadata import AttributeMetadata

class IAttributeMetadataRepository(ABC):
    @abstractmethod
    def get_all(self) -> Dict[str, dict]:
        """Returns the entire metadata for all attributes."""
        pass

    @abstractmethod
    def get_attribute_by_name(self, name: str) -> Optional[dict]:
        """Returns metadata for a specific attribute by name or synonym."""
        pass

    @abstractmethod
    def get_attributes_catalog_names(self) -> List[str]:
        """Returns a list of attribute names in the catalog."""
        pass

    def save_attribute_metadata(self, metadata: List[AttributeMetadata]) -> None:
        """Saves the attribute metadata to the repository."""
        pass