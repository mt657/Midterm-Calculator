"""
Tests for the History class and its methods in the calculator app.

Includes tests for adding, undoing, clearing, saving, and loading history.
"""
# pylint: disable=redefined-outer-name
from unittest.mock import mock_open, patch
import pytest
from app.history import History
from app.calculation import Calculation
from app.operations.addition import Addition
from app.operations.subtraction import Subtraction

# Fixtures
@pytest.fixture
def history():
    """Fixture to initialize a History object for testing."""
    return History()

@pytest.fixture
def sample_calculation():
    """Fixture to create a sample Calculation object."""
    operation = Addition()  # Adjust based on the operation you are testing
    return Calculation(operation=operation, operand1=5, operand2=3)  # No 'result' field here

# Positive Tests
@pytest.mark.parametrize("calculation", [
    Calculation(operation=Addition(), operand1=2, operand2=3),  # Simple addition
    Calculation(operation=Subtraction(), operand1=10, operand2=5),  # Simple subtraction
])
def test_add_calculation(history, calculation):
    """Test adding a calculation to history."""
    history.add_calculation(calculation)
    assert history.get_history()[-1] == calculation  # Ensure the calculation is added

def test_undo_with_history(history, sample_calculation):
    """Test undoing the last calculation when history has items."""
    history.add_calculation(sample_calculation)
    result = history.undo()
    assert result == f"Undone: {sample_calculation}"
    assert not history.get_history()  # History should be empty after undo

def test_clear(history, sample_calculation):
    """Test clearing the calculation history."""
    history.add_calculation(sample_calculation)
    result = history.clear()
    assert result == "History cleared."
    assert not history.get_history()  # History should be empty after clearing

def test_save_load_without_serialization(history, sample_calculation):
    """Test saving and loading history from a file without serialization."""
    # Add the calculation to history
    history.add_calculation(sample_calculation)

    # Mock the open function and the json.dump method to prevent actual file writing
    with patch("builtins.open", mock_open()) as mocked_file, patch("json.dump") as mocked_json_dump:
        # Test the save method
        save_result = history.save("test_history.json")

        # Ensure that save method was called and file was "opened"
        mocked_file.assert_called_once_with("test_history.json", 'w')

        # Ensure that json.dump was called to serialize the history
        mocked_json_dump.assert_called_once_with(
        [calc.__dict__ for calc in history.get_history()], mocked_file())

        # Check the expected result
        assert save_result == "History saved to test_history.json."

    # Prepare mock data to simulate loading from a file
    # Remove the 'result' field from the mock data, as it's not part of Calculation's constructor
    mock_data = '[{"operand1": 5, "operand2": 3, "operation": "Addition"}]'  # No 'result' here

    with patch("builtins.open", mock_open(read_data=mock_data)) as mocked_file, \
    patch("json.load") as mocked_json_load:
        # Mock json.load to return parsed data (instead of loading from file)
        mocked_json_load.return_value = [{'operand1': 5, 'operand2': 3, 'operation': 'Addition'}]

        # Test the load method
        load_result = history.load("test_history.json")

        # Ensure the file is opened
        mocked_file.assert_called_once_with("test_history.json", 'r')

        # Ensure the data was loaded and parsed correctly
        mocked_json_load.assert_called_once_with(mocked_file())

        # Check the expected result
        assert load_result == "History loaded from test_history.json."
        assert len(history.get_history()) == 1  # Ensure one calculation is loaded
        assert history.get_history()[0].operand1 == 5  # Check the calculation data

# Negative Tests
def test_undo_with_empty_history(history):
    """Test undo on an empty history."""
    result = history.undo()
    assert result == "No history to undo."

@pytest.mark.parametrize("filename", ["non_existent.json", "invalid.json"])
def test_load_file_not_found(history, filename):
    """Test loading history from a non-existent file."""
    result = history.load(filename)
    assert result == f"Error: {filename} not found."

def test_load_invalid_json_format(history, tmpdir):
    """Test loading history from a file with invalid JSON data."""
    filename = tmpdir.join("invalid_history.json")

    # Create an invalid JSON file
    with open(str(filename), "w", encoding="utf-8") as file:
        file.write("{invalid json}")  # Corrupted JSON format

    # Match the essential part of the error message
    result = history.load(str(filename))
    assert "Error: Failed to decode history data" in result
