# app/operations/subtraction.py

from app.calculator import Calculator
from typing import Union

class Subtraction(Calculator):
    """Class to perform subtraction of two numbers."""

    def calculate(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Subtract the second number from the first.

        Args:
            a (Union[int, float]): The minuend.
            b (Union[int, float]): The subtrahend.

        Returns:
            float: The difference of the two numbers.
        """
        self._validate_inputs(a, b)  # Validate inputs
        return a - b
