"""Unit tests for the Calculator class."""
# pylint: disable=redefined-outer-name
import pytest
from app.calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance for testing."""
    return Calculator()

@pytest.mark.parametrize("command, args, expected_output", [
    ("add", (1, 2), 3),                          # Positive test
    ("subtract", (5, 3), 2),                     # Positive test
    ("multiply", (2, 4), 8),                     # Positive test
    ("divide", (8, 2), 4),                       # Positive test
    ("divide", (1, 0), "Error: Cannot divide by zero"),  # Negative test
    ("unknown", (1, 2), "Error: Unknown command.")  # Negative test
])
def test_execute_command(calculator, command, args, expected_output):
    """Test the execute_command method for various commands."""
    result = calculator.execute_command(command, *args)

    # Check if the output matches the expected result or error message
    assert result == expected_output

def test_show_help(calculator):
    """Test the show_help method to ensure it returns the correct help text."""
    expected_help_text = (
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
    assert calculator.show_help() == expected_help_text

def test_exit_calculator(calculator):
    """Test the exit_calculator method to ensure it returns the correct exit message."""
    assert calculator.exit_calculator() == "Exiting the calculator. Goodbye!"

def test_exit_command(calculator):
    """Test the exit command to ensure it calls the exit_calculator method."""
    result = calculator.execute_command('exit')
    assert result == "Exiting the calculator. Goodbye!"

def test_invalid_argument_count(calculator):
    """Test handling of invalid argument count."""
    result = calculator.execute_command('add', 1)  # Only one argument
    assert result == "Error: Invalid number of arguments. Please provide two numbers."

    result = calculator.execute_command('add')  # No arguments
    assert result == "Error: Invalid number of arguments. Please provide two numbers."
