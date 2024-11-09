# pylint: disable=redefined-outer-name
import pytest
from app.operation_manager import OperationManager  # Import the OperationManager class


@pytest.fixture
def operation_manager():
    """Fixture to create an OperationManager instance for testing."""
    return OperationManager()


@pytest.mark.parametrize("operation_name, expected_class", [
    ("add", "Addition"),                          # Positive test: Check if 'add' operation is loaded correctly
    ("subtract", "Subtraction"),                  # Positive test: Check if 'subtract' operation is loaded correctly
    ("multiply", "Multiplication"),               # Positive test: Check if 'multiply' operation is loaded correctly
    ("divide", "Division"),                       # Positive test: Check if 'divide' operation is loaded correctly
    ("power", "Power"),                           # Positive test: Check if 'power' operation is loaded correctly
    ("modulus", "Modulus"),                       # Positive test: Check if 'modulus' operation is loaded correctly
])
def test_get_operation(operation_manager, operation_name, expected_class):
    """Test that the get_operation method correctly retrieves the operation class."""
    operation_class = operation_manager.get_operation(operation_name)
    
    # Handle case where operation_class is None (operation not found)
    if operation_class is None:
        pytest.fail(f"Operation class for '{operation_name}' not found.")
    
    # Check if the retrieved operation class name matches the expected class name
    assert operation_class.__name__ == expected_class


@pytest.mark.parametrize("operation_name, expected_list", [
    ("add", ["add", "subtract", "multiply", "divide", "power", "modulus"]),  # Positive test: Check if 'add' is in the list of operations
    ("subtract", ["add", "subtract", "multiply", "divide", "power", "modulus"]),  # Positive test: Check if 'subtract' is in the list
])
def test_list_operations(operation_manager, operation_name, expected_list):
    """Test the list_operations method to check if operations are listed correctly."""
    available_operations = operation_manager.list_operations()
    
    # Check if the list of operations contains the expected operation
    assert operation_name in available_operations
    assert sorted(available_operations) == sorted(expected_list)


@pytest.mark.parametrize("operation_name, expected_output", [
    ("unknown", None),  # Negative test: Check for a non-existent operation
])
def test_get_invalid_operation(operation_manager, operation_name, expected_output):
    """Test the get_operation method when trying to retrieve an invalid operation."""
    result = operation_manager.get_operation(operation_name)
    
    # Assert that the result is None (since the operation is unknown)
    assert result == expected_output
