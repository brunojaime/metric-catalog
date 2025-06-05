import pytest
from repositories.AttributeMetadataRepository.impl.JsonAttributeMetadataRepository import JSONAttributeMetadataRepository
from services.catalog_introspection_service import CatalogIntrospectionService
import json

from services.CatalogService import MetricCatalogService
from services.MetadataCatalogService import MetadataCatalogService

class FakeCatalogRepo:
    def get_catalog(self):
        mock_path = "tests/mock_data/mock_catalog.json"
        with open(mock_path, "r") as f:
            return json.load(f)

@pytest.fixture
def metric_service_mock():
    repo = FakeCatalogRepo()
    svc = MetricCatalogService(repo)
    svc.set_metric_name_field("name")
    return svc


class FakeMetaDataCatalogRepo:
    def get_all(self):
        mock_path = "tests/mock_data/mock_metadata.json"
        with open(mock_path, "r") as f:
            return json.load(f)
        
        
@pytest.fixture
def metadata_service_mock():
    # Simula la carga del catálogo desde un archivo JSON
    mock_path = "tests/mock_data/mock_metadata.json"    
    repo= JSONAttributeMetadataRepository(mock_path)
    return MetadataCatalogService(repo)


def test_combined_attribute_metadata(metric_service_mock, metadata_service_mock):
    service = CatalogIntrospectionService(metric_service_mock, metadata_service_mock)
    result = service.get_combined_attribute_metadata()

    assert isinstance(result, dict)
    assert "name" in result
    assert "type" in result
    assert "description" not in result  # porque no está en el catálogo
    assert "owner" not in result        # porque no está en metadata

    # Opcional: verificar el contenido
    assert result["name"]["description"] == "Metric name"
