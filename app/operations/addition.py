# app/operations/addition.py

from app.operations import Operation
from typing import Union

class Addition(Operation):
    """Class to perform addition of two numbers."""

    def calculate(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Add two numbers.

        Args:
            a (Union[int, float]): The first number.
            b (Union[int, float]): The second number.

        Returns:
            float: The sum of the two numbers.
        """
        self._validate_inputs(a, b)  # Validate inputs
        return a + b
