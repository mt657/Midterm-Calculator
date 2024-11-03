# app/operations/multiplication.py

from app.calculator import Calculator
from typing import Union

class Multiplication(Calculator):
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
