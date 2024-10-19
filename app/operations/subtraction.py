from app.calculator import Calculator

class Subtraction(Calculator):
    """
    Class to perform subtraction of two numbers.
    """

    def calculate(self, a, b):
        """
        Subtract the second number from the first.

        Args:
            a (float): The first number.
            b (float): The second number.
        
        Returns:
            float: The result of the subtraction.
        """
        return a - b
