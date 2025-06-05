import os
import pytest
from dotenv import load_dotenv

from services.MetadataCatalogService import MetadataCatalogService
from repositories.AttributeMetadataRepository.impl.JsonAttributeMetadataRepository import JSONAttributeMetadataRepository

load_dotenv()  

@pytest.fixture
def service_from_env():
    # Simula la carga del catálogo desde un archivo JSON
    mock_path = "tests/mock_data/mock_metadata.json"    
    repo= JSONAttributeMetadataRepository(mock_path)
    return MetadataCatalogService(repo)


def test_get_metadata_fields_success(service_from_env):
    fields = service_from_env.get_metadata_fields()
    assert isinstance(fields, list)
    assert "name" in fields
    assert "type" in fields
    assert "description" in fields 

def test_get_metadata_fields_success(service_from_env):
    fields = service_from_env.get_metadata_fields()
    assert isinstance(fields, list)
    assert "owner" not in fields
    assert "type" in fields
    assert "description" in fields 

def test_get_metadata_fields_empty():
    class EmptyRepo:
        def get_all(self):
            return []  # Simula catálogo vacío

    service = MetadataCatalogService(EmptyRepo())

    with pytest.raises(ValueError, match="Metric catalog is empty"):
        service.get_metadata_fields()
