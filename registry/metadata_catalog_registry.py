import os
from repositories.AttributeMetadataRepository.IAttributeMetadataRepository import IAttributeMetadataRepository
from repositories.AttributeMetadataRepository.impl.JsonAttributeMetadataRepository import JSONAttributeMetadataRepository
from dotenv import load_dotenv

load_dotenv()
class MetadataCatalogRegistry:
    @staticmethod
    def resolve_repository() -> IAttributeMetadataRepository:
        source = os.getenv("METADATA_CATALOG_SOURCE")
        if not source:
            raise ValueError("Missing required env var: METADADATA_CATALOG_SOURCE")

        source = source.lower()

        if source == "json":
            return JSONAttributeMetadataRepository.from_env()
        else:
            raise ValueError(f"Unsupported METADATA_CATALOG_SOURCE: {source}")