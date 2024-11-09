from app.operations import Operation
from typing import Union

class Modulus(Operation):
    """Class to perform modulus (remainder) of two numbers."""

    def calculate(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Perform modulus (remainder of division) operation.

        Args:
            a (Union[int, float]): The dividend.
            b (Union[int, float]): The divisor.

        Returns:
            float: The remainder of a divided by b.
        """
        self._validate_inputs(a, b)  # Validate inputs
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a % b
