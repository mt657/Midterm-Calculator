# app/operations/modulus.py

class Modulus:
    """Class for the modulus operation (remainder of division)."""
    
    def calculate(self, a, b):
        """Calculate the modulus of a divided by b (a % b)."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both operands must be numbers.")
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a % b
