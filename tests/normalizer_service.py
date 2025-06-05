import pytest
from repositories.MetricCatalogRepository.impl.JSONMetricCatalogRepository import JSONMetricCatalogRepository
from repositories.NormalizedCatalogRepository.impl.JSONNormalizedMetricCatalogRepository import JSONNormalizedMetricCatalogRepository
from services.CatalogNormalizerService import CatalogNormalizerService

import json

class FakeCatalogRepo:
    def get_catalog(self):
        mock_path = "tests/mock_data/mock_catalog.json"
        with open(mock_path, "r") as f:
            return json.load(f)
@pytest.fixture
def service():
    cliente_repo = JSONMetricCatalogRepository("tests/mock_data/mock_catalog.json")
    normalized_repo = JSONNormalizedMetricCatalogRepository("tests/mock_data/mock_normalized_catalog.json")
    return CatalogNormalizerService(cliente_repo, normalized_repo)

def test_generate_normalized_catalog(service):
    service.generate_normalized_catalog()
    normalized_catalog = service.normalized_repo.get_catalog()
    
    assert len(normalized_catalog) > 0
    assert all("name" in metric for metric in normalized_catalog)
   # assert all("normalized_name" in metric for metric in normalized_catalog)
    