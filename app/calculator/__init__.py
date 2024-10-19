from abc import ABC, abstractmethod

class Calculator(ABC):
    """Abstract base class for a calculator with a general abstract calculate method."""

    @abstractmethod
    def calculate(self, a, b):
        """
        Abstract method to perform a calculation.
        Subclasses must implement this method.
        """
        pass # pragma: no cover
