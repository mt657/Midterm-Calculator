"""
Tests for the History class in the app.history module.

This module tests the functionality of the History class, including loading, 
saving, adding, undoing, and clearing calculations. It also checks error handling 
for empty, non-existent, and corrupted files.

Fixtures:
    history: Provides a fresh instance of the History class for each test.
"""
# pylint: disable=redefined-outer-name
from unittest.mock import patch, MagicMock
import pytest
import pandas as pd
from app.history import History
from app.calculation import Calculation
from app.operations.addition import Addition
import os

# Sample data for testing purposes
sample_calculation = Calculation(Addition(), 5, 3)
sample_calculation.set_result(8)

# Path to the history file to be used in tests
HISTORY_FILE_PATH = "history.csv"

# Function to ensure the history file is clean before each test
def clean_history_file():
    """Remove the history file if it exists to ensure a clean slate for each test."""
    if os.path.exists(HISTORY_FILE_PATH):
        os.remove(HISTORY_FILE_PATH)


@pytest.fixture
def history_fixture():
    """Fixture to provide an instance of the History class."""
    clean_history_file()  # Clean the history file before each test
    yield History()  # Return the History instance to be used in tests
    clean_history_file()  # Clean the history file after the test is done


@pytest.mark.parametrize("filename, expected_error_msg", [
    ("empty.csv", "Error: empty.csv is empty or corrupted.")
])
def test_load_empty_file(history_fixture, filename, expected_error_msg):
    """Test case for loading an empty file."""
    with patch("os.path.exists", return_value=True):
        with patch("pandas.read_csv", return_value=MagicMock(empty=True)):
            history_fixture.filename = filename
            load_msg = history_fixture.load()
            assert load_msg == expected_error_msg


@pytest.mark.parametrize("filename, expected_error_msg", [
    ("non_existent.csv", "Error: non_existent.csv not found.")
])
def test_load_non_existent_file(history_fixture, filename, expected_error_msg):
    """Test case for loading a non-existent file."""
    with patch("os.path.exists", return_value=False):
        history_fixture.filename = filename
        load_msg = history_fixture.load()
        assert load_msg == expected_error_msg


def test_add_calculation(history_fixture):
    """Test case for adding a calculation to history."""
    history_fixture.add_calculation(sample_calculation)
    assert len(history_fixture.get_history()) == 1


@pytest.mark.parametrize("filename, expected_error_msg", [
    ("corrupted.csv", "Error: corrupted.csv is empty or corrupted.")
])
def test_load_corrupted_file(history_fixture, filename, expected_error_msg):
    """Test case for loading a corrupted file."""
    with patch("os.path.exists", return_value=True):
        with patch("pandas.read_csv", side_effect=pd.errors.EmptyDataError):
            history_fixture.filename = filename
            load_msg = history_fixture.load()
            assert load_msg == expected_error_msg


def test_undo_calculation(history_fixture):
    """Test case for undoing a calculation."""
    history_fixture.add_calculation(sample_calculation)
    undo_msg = history_fixture.undo()
    assert undo_msg == f"Undone: {sample_calculation}"
    assert len(history_fixture.get_history()) == 0  # The history should be empty after undo


def test_clear_calculation_history(history_fixture):
    """Test case for clearing the calculation history."""
    history_fixture.add_calculation(sample_calculation)
    history_fixture.clear()
    assert len(history_fixture.get_history()) == 0  # The history should be cleared


@pytest.mark.parametrize("expected_msg", [
    "History saved to history.csv."
])
def test_save_calculation_history(history_fixture, expected_msg):
    """Test case for saving the calculation history."""
    history_fixture.add_calculation(sample_calculation)
    with patch("pandas.DataFrame.to_csv") as mock_to_csv:
        save_msg = history_fixture.save()
        assert save_msg == expected_msg
        mock_to_csv.assert_called_once_with("history.csv", index=False)  # Ensure to_csv was called


def test_load_history_success(history_fixture):
    """Test case for loading the history successfully."""
    with patch("os.path.exists", return_value=True):
        with patch(
            "pandas.read_csv", 
            return_value=MagicMock(empty=False,
               iterrows=MagicMock(return_value=[(0, {"operand1": 5,
                    "operation": "Addition", "operand2": 3, "result": 8})]))):
            history_fixture.load()
            assert len(history_fixture.get_history()) == 1  # One calculation should be loaded


def test_load_exception_handling(history_fixture):
    """Test case for handling general exceptions during file load."""
    with patch("pandas.read_csv", side_effect=Exception("Test exception")):
        load_msg = history_fixture.load()
        # Verify the error message returned matches the exception
        assert load_msg == "Error: Test exception"


def test_load_unknown_operation(history_fixture):
    """Test case for handling unknown operations during load."""
    # Mock the pandas read_csv method to return a row with an unknown operation
    with patch("pandas.read_csv", return_value=MagicMock(empty=False,
        iterrows=MagicMock(return_value=[(0, {"operand1": 5,
            "operation": "UnknownOperation", "operand2": 3, "result": 8})]))):
        
        # Catch the log output
        with patch('app.history.logger') as mock_logger:
            load_msg = history_fixture.load()

            # Check that the log call for unknown operation is made
            mock_logger.error.assert_called_with("Operation UnknownOperation not recognized during load.")
            
            # Check that the load method returns the error message for an unknown operation
            assert load_msg == "Error: Operation UnknownOperation not recognized."


def test_undo_no_history(history_fixture):
    """Test case for undoing when there is no history."""
    assert len(history_fixture.get_history()) == 0  # History should be empty
    undo_msg = history_fixture.undo()
    assert undo_msg == "No history to undo."  # Ensure the correct message is returned

# Test case to ensure the correct handling of ValueError during history loading
def test_load_history_invalid_data():
    # Prepare mock data for an invalid CSV (non-numeric values)
    invalid_data = {
        "operand1": ["a", "b", "c"],  # Non-numeric values
        "operation": ["Addition", "Subtraction", "Multiplication"],
        "operand2": ["d", "e", "f"],  # Non-numeric values
        "result": ["x", "y", "z"]     # Non-numeric values
    }
    # Convert the mock data into a DataFrame
    df_invalid = pd.DataFrame(invalid_data)
    
    # Mock pandas.read_csv to return the invalid DataFrame
    with patch('pandas.read_csv', return_value=df_invalid):
        # Create a History instance
        history = History()
        
        # Capture the output from the load method
        result = history.load()

        # Check if the appropriate error message is returned
        assert result == "Error: Invalid data in history.csv."
        
        # Additionally, we can check that logging occurred
        with patch('app.history.logger.error') as mock_error:
            history.load()
            mock_error.assert_called_with("Error processing row: could not convert string to float: 'a'")
