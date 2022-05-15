from abc import ABC, abstractmethod


class FoodCreator(ABC):
    """
    Abstract factory for classes
    """
    @abstractmethod
    def factory_method(self):
        pass

    def create(self, name):
        """
        Creates food by name
        """
        food = self.factory_method(name)
        return food
