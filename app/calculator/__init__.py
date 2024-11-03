from app.operations.addition import Addition
from app.operations.subtraction import Subtraction
from app.operations.multiplication import Multiplication
from app.operations.division import Division

class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    def __init__(self):
        """Initialize the Calculator with command mappings.

        Maps user commands to their respective operation functions.
        """
        self.commands = {
            'add': Addition().calculate,
            'subtract': Subtraction().calculate,
            'multiply': Multiplication().calculate,
            'divide': Division().calculate,
            'help': self.show_help,
            'exit': self.exit_calculator,
            'quit': self.exit_calculator
        }

    def execute_command(self, command, *args):
        """Execute the command associated with the user input.

        Args:
            command (str): The command to execute (e.g., 'add', 'subtract').
            *args: Variable length argument list for the operation's operands.

        Returns:
            str: The result of the operation or an error message if an error occurs.
        """
        if command in self.commands:
            try:
                if command in ['exit', 'quit']:
                    return self.commands[command]()  # Call the exit method
                return self.commands[command](*args)  # Return the operation result
            except TypeError:
                return "Error: Invalid number of arguments. Please provide two numbers."
            except Exception as e:
                return f"Error: {str(e)}"
        else:
            return "Error: Unknown command."

    def show_help(self):
        """Display available commands in a readable format.

        Returns:
            str: A formatted string of available commands for the user.
        """
        help_text = (
            "Available commands:\n"
            "\n"
            "- add: Add two numbers\n"
            "- subtract: Subtract the second number from the first\n"
            "- multiply: Multiply two numbers\n"
            "- divide: Divide the first number by the second\n"
            "- help: Display this help message\n"
            "- exit/quit: Exit the calculator"
        )
        return help_text

    def exit_calculator(self):
        """Exit the calculator.

        Returns:
            str: A farewell message indicating the calculator is closing.
        """
        return "Exiting the calculator. Goodbye!"
