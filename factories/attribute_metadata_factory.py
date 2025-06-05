from typing import List
from models.AttributeMetadata import AttributeMetadata

class AttributeMetadataFactory:
    @staticmethod
    def build_from_display_names(display_names: List[str]) -> List[AttributeMetadata]:
        return [AttributeMetadata.from_display_name(name) for name in display_names]
