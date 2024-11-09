# app/operations/power.py

class Power:
    """Class for the power operation (exponentiation)."""
    
    def calculate(self, a, b):
        """Calculate a raised to the power of b (a^b)."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both operands must be numbers.")
        return a ** b
