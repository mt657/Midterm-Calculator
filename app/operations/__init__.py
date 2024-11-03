from abc import ABC, abstractmethod
from typing import Union

class Operation(ABC):
    """Abstract base class for a calculator with a general abstract calculate method."""

    def _validate_inputs(self, a: Union[int, float], b: Union[int, float]) -> None:
        """
        Validate input types for calculation.

        Args:
            a (Union[int, float]): The first input.
            b (Union[int, float]): The second input.

        Raises:
            TypeError: If either a or b is not a number (int or float).
        """
        if not all(isinstance(arg, (int, float)) for arg in (a, b)):
            raise TypeError(f"Invalid types: a is {type(a).__name__}, b is {type(b).__name__}. Expected int or float.")

    @abstractmethod
    def calculate(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Abstract method to perform a calculation.
        Subclasses must implement this method.

        Args:
            a (Union[int, float]): The first number.
            b (Union[int, float]): The second number.

        Returns:
            float: The result of the calculation.
        """
        pass  # pragma: no cover
