from abc import ABC, abstractmethod

class Step(ABC):
    """Abstract pipeline step."""

    @abstractmethod
    def run(self, data: dict) -> dict:
        """Takes data dict, returns updated data dict."""
        pass
