from repositories.NormalizedCatalogRepository import INormalizedMetricCatalogRepository


class MemoryAttributeListRepository(INormalizedMetricCatalogRepository):
    def __init__(self):
        self._attribute_list = []

    def save_attribute_list(self, attribute_list: list[str]) -> None:
        """
        Save a list of attributes in memory.
        
        :param attribute_list: List of attributes to save.
        """
        self._attribute_list = attribute_list

    def load_attribute_list(self) -> list[str]:
        """
        Load the list of attributes from memory.
        
        :return: List of attributes.
        """
        return self._attribute_list.copy()  # Return a copy to prevent external modifications