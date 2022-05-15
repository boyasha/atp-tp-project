from abc import ABC, abstractmethod


class FoodCreator(ABC):
    """
    Abstract factory for classes
    """
    @abstractmethod
    def factory_method(self, display_size):
        pass

    def create(self, display_size):
        """
        Creates food by name
        """
        food = self.factory_method(display_size)
        return food
