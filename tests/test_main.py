# tests/test_main.py

"""Tests for the main module and its functions."""

from io import StringIO
from unittest.mock import patch
from main import main, center_text
from app.calculator import Calculator

def test_center_text():
    """Test the center_text function to ensure it centers text correctly."""
    expected_output = "       Hello        "
    assert center_text("Hello", 20) == expected_output

@patch('sys.stdout', new_callable=StringIO)
def test_main_negative(mock_stdout):
    """Test the main function for negative cases, handling various command inputs."""
    # Define a sequence of inputs to simulate user interactions
    inputs = iter(['add 1 2', 'divide 1 0', 'unknown command', 'exit'])

    # Use side_effect with a lambda that takes an argument to match input's call signature
    with patch('builtins.input', side_effect=lambda _: next(inputs)):
        main()

    output = mock_stdout.getvalue()

    # Checking for expected outputs in sequence
    assert "Result: 3.0" in output  # Expected result of 'add 1 2'
    assert "Error: Cannot divide by zero" in output  # Expected error for division by zero
    assert "Error: Invalid input." in output  # Expected error for unknown command
    assert "Exiting the calculator. Goodbye!" in output  # Final exit message

@patch('sys.stdout', new_callable=StringIO)
def test_main_with_history(mock_stdout):
    """Test the main function when a list output (e.g., history) is returned."""

    # Simulate a list of history items returned by the Calculator
    history_items = ["1 + 1 = 2", "2 + 3 = 5", "5 - 1 = 4"]

    # Mock the 'execute_command' method to return a history list
    with patch.object(Calculator, 'execute_command', return_value=history_items):
        inputs = iter(['history', 'exit'])  # Simulate the command 'history' followed by 'exit'
        with patch('builtins.input', side_effect=lambda _: next(inputs)):
            main()

    output = mock_stdout.getvalue()

    # Check if the history items are printed centered
    for item in history_items:
        assert item.center(50) in output  # The history item should be printed centered

    assert "Exiting the calculator. Goodbye!" in output  # Ensure the exit message is printed
