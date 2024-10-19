from app.calculator import Calculator

class Addition(Calculator):
    """
    Class to perform addition of two numbers.
    """

    def calculate(self, a, b):
        """
        Add two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.
        
        Returns:
            float: The sum of the two numbers.
        """
        return a + b
