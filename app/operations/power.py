from app.operations import Operation
from typing import Union

class Power(Operation):
    """Class to perform exponentiation (power) of two numbers."""

    def calculate(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Perform exponentiation (a raised to the power of b).

        Args:
            a (Union[int, float]): The base.
            b (Union[int, float]): The exponent.

        Returns:
            float: The result of a raised to the power of b.
        """
        self._validate_inputs(a, b)  # Validate inputs
        return a ** b
