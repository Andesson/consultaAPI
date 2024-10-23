from abc import ABC, abstractmethod

class APIInterface(ABC):
    @abstractmethod
    def query(self, params=None):
        pass
