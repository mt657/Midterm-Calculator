import pytest
import importlib

# List of operation names to be dynamically imported
operation_names = [
    "addition",
    "subtraction",
    "multiplication",
    "division",
    "power",
    "modulus",
]

# Mapping operations to their respective expected results
operation_map = {
    "addition": [
        (3, 5, 8),
        (-1, 1, 0),
        (0, 0, 0),
    ],
    "subtraction": [
        (10, 5, 5),
        (5, 10, -5),
        (0, 0, 0),
    ],
    "multiplication": [
        (3, 7, 21),
        (-1, 10, -10),
        (0, 5, 0),
    ],
    "division": [
        (10, 2, 5),
        (5, 2, 2.5),
        (0, 1, 0),
    ],
    "power": [
        (2, 3, 8),    # 2^3 = 8
        (3, 2, 9),    # 3^2 = 9
        (5, 0, 1),    # 5^0 = 1
    ],
    "modulus": [
        (10, 3, 1),   # 10 % 3 = 1
        (7, 2, 1),    # 7 % 2 = 1
        (5, 5, 0),    # 5 % 5 = 0
    ],
}

# Generic fixture that returns instances of operation classes dynamically
@pytest.fixture
def operation(request):
    """Fixture to dynamically import and provide an instance of the operation class."""
    operation_name = request.param  # Get the operation name
    module_name = f"app.operations.{operation_name}"  # Construct module name dynamically
    operation_module = importlib.import_module(module_name)  # Import the module dynamically
    operation_class = getattr(operation_module, operation_name.capitalize())  # Get the class dynamically
    return operation_class()

# Parametrize the test cases dynamically
@pytest.mark.parametrize("operation_name, a, b, expected", [
    ("addition", 3, 5, 8),
    ("addition", -1, 1, 0),
    ("addition", 0, 0, 0),
    ("subtraction", 10, 5, 5),
    ("subtraction", 5, 10, -5),
    ("subtraction", 0, 0, 0),
    ("multiplication", 3, 7, 21),
    ("multiplication", -1, 10, -10),
    ("multiplication", 0, 5, 0),
    ("division", 10, 2, 5),
    ("division", 5, 2, 2.5),
    ("division", 0, 1, 0),
    ("power", 2, 3, 8),        # Test power operation: 2^3 = 8
    ("power", 3, 2, 9),        # Test power operation: 3^2 = 9
    ("power", 5, 0, 1),        # Test power operation: 5^0 = 1
    ("modulus", 10, 3, 1),     # Test modulus operation: 10 % 3 = 1
    ("modulus", 7, 2, 1),      # Test modulus operation: 7 % 2 = 1
    ("modulus", 5, 5, 0),      # Test modulus operation: 5 % 5 = 0
])
def test_operations(operation, operation_name, a, b, expected):
    """Test the basic arithmetic operations (addition, subtraction, multiplication, division, power, modulus)."""
    operation_instance = operation  # Get the operation instance from the fixture
    assert operation_instance.calculate(a, b) == expected

@pytest.mark.parametrize("operation_name, a, b", [
    ("addition", 5, 'x'),      # Invalid input type: string instead of number
    ("addition", 'y', 3),      # Invalid input type: string instead of number
    ("addition", None, 4),     # Invalid input type: None
    ("subtraction", 5, 'z'),   # Invalid input type: string instead of number
    ("subtraction", 'x', 3),   # Invalid input type: string instead of number
    ("subtraction", None, 4),  # Invalid input type: None
    ("multiplication", 3, 'x'), # Invalid input type: string instead of number
    ("multiplication", 'y', 3), # Invalid input type: string instead of number
    ("multiplication", None, 4), # Invalid input type: None
    ("division", 5, 'z'),      # Invalid input type: string instead of number
    ("division", 'x', 5),      # Invalid input type: string instead of number
    ("division", None, 5),     # Invalid input type: None
    ("power", 2, 'x'),         # Invalid input type: string instead of number
    ("power", 'y', 3),         # Invalid input type: string instead of number
    ("modulus", 5, 'z'),       # Invalid input type: string instead of number
    ("modulus", 'x', 5),       # Invalid input type: string instead of number
])
def test_operations_invalid(operation, operation_name, a, b):
    """Test that operations raise TypeError for invalid inputs."""
    with pytest.raises(TypeError):
        operation_instance = operation  # Get the operation instance from the fixture
        operation_instance.calculate(a, b)

def test_division_by_zero(division_fixture):
    """Test that division by zero raises a ValueError."""
    with pytest.raises(ValueError):
        division_fixture.calculate(5, 0)
