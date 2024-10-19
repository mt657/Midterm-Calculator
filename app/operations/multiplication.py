from app.calculator import Calculator

class Multiplication(Calculator):
    """
    Class to perform multiplication of two numbers.
    """

    def calculate(self, a, b):
        """
        Multiply two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.
        
        Returns:
            float: The product of the two numbers.
        """
        return a * b
