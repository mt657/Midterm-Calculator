from app.calculator import Calculator

class Division(Calculator):
    """
    Class to perform division of two numbers.
    """

    def calculate(self, a, b):
        """
        Divide the first number by the second.

        Args:
            a (float): The numerator.
            b (float): The denominator.
        
        Returns:
            float: The result of the division.
        
        Raises:
            ValueError: If the denominator (b) is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
