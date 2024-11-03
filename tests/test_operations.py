# pylint: disable=redefined-outer-name
"""
Test suite for calculator operations including addition, subtraction,
multiplication, and division operations.
"""

import pytest
from app.operations.addition import Addition
from app.operations.subtraction import Subtraction
from app.operations.multiplication import Multiplication
from app.operations.division import Division

@pytest.fixture
def addition_fixture():
    """Fixture that provides an instance of the Addition class."""
    return Addition()

@pytest.fixture
def subtraction_fixture():
    """Fixture that provides an instance of the Subtraction class."""
    return Subtraction()

@pytest.fixture
def multiplication_fixture():
    """Fixture that provides an instance of the Multiplication class."""
    return Multiplication()

@pytest.fixture
def division_fixture():
    """Fixture that provides an instance of the Division class."""
    return Division()

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),      # Test case: 3 + 5 should return 8
    (-1, 1, 0),    # Test case: -1 + 1 should return 0
    (0, 0, 0),     # Test case: 0 + 0 should return 0
])
def test_addition(addition_fixture, a, b, expected):
    """Test the addition operation with valid integer inputs."""
    assert addition_fixture.calculate(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),     # Test case: 10 - 5 should return 5
    (5, 10, -5),    # Test case: 5 - 10 should return -5
    (0, 0, 0),      # Test case: 0 - 0 should return 0
])
def test_subtraction(subtraction_fixture, a, b, expected):
    """Test the subtraction operation with valid integer inputs."""
    assert subtraction_fixture.calculate(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 7, 21),     # Test case: 3 * 7 should return 21
    (-1, 10, -10),  # Test case: -1 * 10 should return -10
    (0, 5, 0),      # Test case: 0 * 5 should return 0
])
def test_multiplication(multiplication_fixture, a, b, expected):
    """Test the multiplication operation with valid integer inputs."""
    assert multiplication_fixture.calculate(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),     # Test case: 10 / 2 should return 5
    (5, 2, 2.5),    # Test case: 5 / 2 should return 2.5
    (0, 1, 0),      # Test case: 0 / 1 should return 0
])
def test_division(division_fixture, a, b, expected):
    """Test the division operation with valid integer inputs."""
    assert division_fixture.calculate(a, b) == expected

def test_division_by_zero(division_fixture):
    """Test that division by zero raises a ValueError."""
    with pytest.raises(ValueError):
        division_fixture.calculate(5, 0)

@pytest.mark.parametrize("a, b", [
    (5, 'x'),      # Invalid input type: string instead of number
    ('y', 3),      # Invalid input type: string instead of number
    (None, 4),     # Invalid input type: None
])
def test_addition_invalid(addition_fixture, a, b):
    """Test that addition raises TypeError for invalid inputs."""
    with pytest.raises(TypeError):
        addition_fixture.calculate(a, b)

@pytest.mark.parametrize("a, b", [
    (5, 'z'),      # Invalid input type: string instead of number
    ('x', 3),      # Invalid input type: string instead of number
    (None, 4),     # Invalid input type: None
])
def test_subtraction_invalid(subtraction_fixture, a, b):
    """Test that subtraction raises TypeError for invalid inputs."""
    with pytest.raises(TypeError):
        subtraction_fixture.calculate(a, b)

@pytest.mark.parametrize("a, b", [
    (3, 'x'),      # Invalid input type: string instead of number
    ('y', 3),      # Invalid input type: string instead of number
    (None, 4),     # Invalid input type: None
])
def test_multiplication_invalid(multiplication_fixture, a, b):
    """Test that multiplication raises TypeError for invalid inputs."""
    with pytest.raises(TypeError):
        multiplication_fixture.calculate(a, b)

@pytest.mark.parametrize("a, b", [
    (5, 'z'),      # Invalid input type: string instead of number
    ('x', 5),      # Invalid input type: string instead of number
    (None, 5),     # Invalid input type: None
])
def test_division_invalid(division_fixture, a, b):
    """Test that division raises TypeError for invalid inputs."""
    with pytest.raises(TypeError):
        division_fixture.calculate(a, b)
