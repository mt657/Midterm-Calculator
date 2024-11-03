# app/operations/multiplication.py

from app.operations import Operation
from typing import Union

class Multiplication(Operation):
    """Class to perform multiplication of two numbers."""

    def calculate(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Multiply two numbers.

        Args:
            a (Union[int, float]): The first number.
            b (Union[int, float]): The second number.

        Returns:
            float: The product of the two numbers.
        """
        self._validate_inputs(a, b)  # Validate inputs
        return a * b
