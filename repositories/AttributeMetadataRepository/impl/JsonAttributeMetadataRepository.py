import json
from typing import List, Dict, Optional
from repositories.AttributeMetadataRepository.IAttributeMetadataRepository import IAttributeMetadataRepository
import os

class JSONAttributeMetadataRepository(IAttributeMetadataRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path


    @staticmethod
    def from_env() -> 'JSONAttributeMetadataRepository':
        path = os.getenv("METADATA_CATALOG_PATH")
        if not path:
            raise ValueError("Not metadata path provided in environment variable METADATA_PATH")
        return JSONAttributeMetadataRepository(path)

    def get_all(self) -> List[dict]:
        with open(self.file_path, "r") as f:
            return json.load(f)
        
    def get_attribute_by_name(self, attribute_name: str) -> Optional[Dict[str, str]]:
        metadata = self.get_all()
        return metadata.get(attribute_name, None)
    
    def get_attributes_catalog_names(self) -> List[str]:
        metadata = self.get_all()
        return list(metadata.keys())