import pytest
from services.CatalogService import MetricCatalogService
import json
# Fake repo para testear sin archivos reales
class FakeCatalogRepo:
    def get_catalog(self):
        mock_path = "tests/mock_data/mock_catalog.json"
        with open(mock_path, "r") as f:
            return json.load(f)
 


    def get_metric_by_name(self, field_name, value):
        for item in self.get_catalog():
            name_value = item.get(field_name, "").strip().lower()
            if name_value == value:
                return item
        return None


@pytest.fixture
def service():
    repo = FakeCatalogRepo()
    svc = MetricCatalogService(repo)
    svc.set_metric_name_field("name")
    return svc


def test_get_readable_catalog(service):
    result = service.get_readable_catalog()
    assert "Headcount - Total active employees" in result
    assert "Attrition Rate - Percentage of employees who left" in result


def test_get_attribute_fields(service):
    fields = service.get_attribute_fields()
    assert "name" in fields
    assert "owner" in fields
    assert isinstance(fields, list)



def test_get_catalog_selected_fields_valid(service):
    selected = service.get_catalog_selected_fields(["name", "owner"])
    assert isinstance(selected, list)
    assert all("name" in row and "owner" in row for row in selected)


def test_get_catalog_selected_fields_invalid(service):
    with pytest.raises(ValueError, match="Unknown fields: fake_field"):
        service.get_catalog_selected_fields(["name", "fake_field"])


def test_get_metric_found(service):
    result = service.get_metric("headcount")
    assert result["name"] == "Headcount"


def test_get_metric_not_found(service):
    with pytest.raises(ValueError, match="Metric 'foo' not found."):
        service.get_metric("foo")


def test_get_metric_with_attributes(service):
    result = service.get_metric("headcount", ["owner"])
    assert result == {"owner": "HR"}
