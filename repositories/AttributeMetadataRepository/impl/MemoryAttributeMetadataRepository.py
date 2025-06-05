from typing import Dict, Optional, List
from repositories.AttributeMetadataRepository import IAttributeMetadataRepository
from models.AttributeMetadata import AttributeMetadata


class InMemoryAttributeMetadataRepository(IAttributeMetadataRepository):
    def __init__(self):
        self._data: Dict[str, AttributeMetadata] = {}

    def save_attribute_metadata(self, attribute: AttributeMetadata) -> None:
        if not attribute.attribute_id:
            raise ValueError("Attribute must have an attribute_id.")
        self._data[attribute.attribute_id] = attribute

    def get_all(self) -> Dict[str, dict]:
        return {k: v.to_dict() for k, v in self._data.items()}


    def get_attribute_by_name(self, name: str) -> AttributeMetadata:
        normalized = name.strip().lower()
        if normalized in self._data:
            return self._data[normalized]

        for attr in self._data.values():
            if normalized in [s.lower() for s in attr.synonyms or []]:
                return attr

        raise ValueError(f"Attribute '{name}' not found.")



    def get_attributes_catalog_names(self) -> List[str]:
        return list(self._data.keys())
