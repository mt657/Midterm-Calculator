from app.operations.addition import Addition
from app.operations.subtraction import Subtraction
from app.operations.multiplication import Multiplication
from app.operations.division import Division
from app.history import History
from app.calculation import Calculation

class Calculator:
    """A simple calculator class to perform basic arithmetic operations with history tracking."""

    def __init__(self):
        """Initialize the Calculator with command mappings and history."""
        self.history = History()  # Initialize history attribute here
        self.commands = {
            'add': Addition(),
            'subtract': Subtraction(),
            'multiply': Multiplication(),
            'divide': Division(),
            'help': self.show_help,
            'exit': self.exit_calculator,
            'quit': self.exit_calculator,
            'undo': self.history.undo,
            'clear': self.history.clear,
            'save': self.history.save,
            'load': self.history.load,  # Ensure load command maps to load_history
            'history': self.history.get_history
        }

    def execute_command(self, command, *args):
        """Execute the command associated with the user input.

        Args:
            command (str): The command to execute (e.g., 'add', 'subtract').
            *args: Variable length argument list for the operation's operands.

        Returns:
            str or float: The result of the operation, or an error message if an error occurs.
        """
        if command in self.commands:
            try:
                if command in ['exit', 'quit', 'undo', 'clear', 'help', 'save', 'load', 'history']:
                    return self.commands[command]()  # Directly return result for non-math commands

                # Create a Calculation instance, perform the operation, and add to history
                operation = self.commands[command]
                calculation = Calculation(operation, *args)
                result = calculation.execute()
                self.history.add_calculation(calculation)  # Log calculation to history
                return result  # Return only the numeric result

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
            "Operation Commands:\n"
            "- add: Add two numbers\n"
            "- subtract: Subtract the second number from the first\n"
            "- multiply: Multiply two numbers\n"
            "- divide: Divide the first number by the second\n"
            "\n"
            "History Commands:\n"
            "- undo: Undo the last calculation\n"
            "- clear: Clear the calculation history\n"
            "- history: Read the calculation history\n"
            "\n"
            "File Commands:\n"
            "- save: Save the current history to a file\n"
            "- load: Load history from a file\n"
            "\n"
            "General Commands:\n"
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
