from unittest.mock import MagicMock, patch
import pytest
from main import main, center_text  # Import from root directory

# Mocking OperationManager and any related functionality
@pytest.fixture(autouse=True)
def mock_operation_manager(monkeypatch):
    # Patch the OperationManager import to prevent actual operation management during tests
    mock_manager = MagicMock()
    monkeypatch.setattr("app.calculator.OperationManager", mock_manager)
    monkeypatch.setattr("app.calculator.load_operations", MagicMock(return_value={}))  # Mock load_operations too


@pytest.mark.parametrize(
    "command, args, expected_output",
    [
        ("add", ['3', '4'], "Result: 7.0"),
        ("subtract", ['10', '4'], "Result: 6.0"),
        ("multiply", ['3', '5'], "Result: 15.0"),
        ("divide", ['10', '2'], "Result: 5.0"),
        ("divide", ['10', '0'], "Error: Cannot divide by zero"),
    ]
)
def test_main_operations(mock_input, capsys, command, args, expected_output):
    """Test the main loop for various operations (add, subtract, multiply, divide)."""
    mock_input([command] + args)  # Mock user input for command and arguments

    # Run the main function (simulates the interactive loop)
    main()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the expected output is in the captured stdout
    assert expected_output in captured.out


@pytest.mark.parametrize(
    "command, expected_output",
    [
        ("exit", "Exiting the calculator. Goodbye!"),
        ("quit", "Exiting the calculator. Goodbye!"),
        ("help", "Available commands:")
    ]
)
def test_main_commands(mock_input, capsys, command, expected_output):
    """Test the main loop for special commands (exit, quit, help)."""
    mock_input([command])

    # Run the main function (simulates the interactive loop)
    with pytest.raises(SystemExit):  # Expect the main function to exit for exit/quit
        main()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the expected output is in the captured stdout
    assert expected_output in captured.out


@pytest.mark.parametrize(
    "user_input, expected_error_message",
    [
        (['add', 'a', 'b'], "Error: Invalid input."),
        (['subtract', '10'], "Error: Invalid input."),
        (['multiply', 'x', 'y'], "Error: Invalid input."),
    ]
)
def test_main_invalid_input(mock_input, capsys, user_input, expected_error_message):
    """Test the main loop for invalid inputs."""
    mock_input(user_input)

    # Run the main function (simulates the interactive loop)
    main()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the expected error message is printed
    assert expected_error_message in captured.out


@pytest.mark.parametrize(
    "text, width, expected_centered_text",
    [
        ("Hello", 20, "       Hello        "),
        ("Python", 30, "            Python            "),
        ("Test", 10, "    Test    "),
    ]
)
def test_center_text(text, width, expected_centered_text):
    """Test the center_text function for various inputs."""
    centered_text = center_text(text, width)
    assert centered_text == expected_centered_text
