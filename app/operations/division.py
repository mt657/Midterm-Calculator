# app/operations/division.py

from app.calculator import Calculator
from typing import Union

class Division(Calculator):
    """Class to perform division of two numbers."""

    def calculate(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Divide the first number by the second.

        Args:
            a (Union[int, float]): The numerator.
            b (Union[int, float]): The denominator.

        Returns:
            float: The result of the division.

        Raises:
            ValueError: If the denominator (b) is zero.
        """
        self._validate_inputs(a, b)  # Validate inputs
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
