from typing import Union
from app.operations import Operation

class Calculation:
    """Class to represent a single calculation with an operation and two operands."""

    def __init__(self, operation: Operation, operand1: Union[int, float], operand2: Union[int, float]):
        """
        Initialize a calculation with an operation and two operands.

        Args:
            operation (Operation): An instance of an Operation subclass (e.g., Addition, Subtraction).
            operand1 (Union[int, float]): The first operand for the calculation.
            operand2 (Union[int, float]): The second operand for the calculation.
        """
        self.operation = operation  # Store the Operation instance (e.g., Addition, Subtraction)
        self.operand1 = operand1  # Store the first operand
        self.operand2 = operand2  # Store the second operand
        self.result: Union[int, float, None] = None  # Initialize the result as None until calculated

    def execute(self) -> Union[int, float]:
        """
        Perform the calculation using the provided operation and operands, then store the result.

        Returns:
            Union[int, float]: The result of the calculation after execution.
        """
        self.result = self.operation.calculate(self.operand1, self.operand2)  # Perform the calculation using the operation
        return self.result

    def __repr__(self) -> str:
        """
        Provide a string representation of the calculation, showing operands, operation, and result.

        Returns:
            str: A formatted string showing the operands, operation, and result (if calculated).
        """
        return f"{self.operand1} {self.operation.__class__.__name__.lower()} {self.operand2} = {self.result if self.result is not None else 'Not calculated'}"
