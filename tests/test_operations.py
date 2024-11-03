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
    """Fixture for the Addition class."""
    return Addition()

@pytest.fixture
def subtraction_fixture():
    """Fixture for the Subtraction class."""
    return Subtraction()

@pytest.fixture
def multiplication_fixture():
    """Fixture for the Multiplication class."""
    return Multiplication()

@pytest.fixture
def division_fixture():
    """Fixture for the Division class."""
    return Division()

@pytest.mark.parametrize("input_a, input_b, expected", [
    (3, 5, 8),      # 3 + 5 = 8
    (-1, 1, 0),     # -1 + 1 = 0
    (0, 0, 0),      # 0 + 0 = 0
])
def test_addition(addition_fixture, input_a, input_b, expected):
    """Test the addition operation."""
    assert addition_fixture.calculate(input_a, input_b) == expected

@pytest.mark.parametrize("input_a, input_b, expected", [
    (10, 5, 5),     # 10 - 5 = 5
    (5, 10, -5),    # 5 - 10 = -5
    (0, 0, 0),      # 0 - 0 = 0
])
def test_subtraction(subtraction_fixture, input_a, input_b, expected):
    """Test the subtraction operation."""
    assert subtraction_fixture.calculate(input_a, input_b) == expected

@pytest.mark.parametrize("input_a, input_b, expected", [
    (3, 7, 21),     # 3 * 7 = 21
    (-1, 10, -10),  # -1 * 10 = -10
    (0, 5, 0),      # 0 * 5 = 0
])
def test_multiplication(multiplication_fixture, input_a, input_b, expected):
    """Test the multiplication operation."""
    assert multiplication_fixture.calculate(input_a, input_b) == expected

@pytest.mark.parametrize("input_a, input_b, expected", [
    (10, 2, 5),     # 10 / 2 = 5
    (5, 2, 2.5),    # 5 / 2 = 2.5
    (0, 1, 0),      # 0 / 1 = 0
])
def test_division(division_fixture, input_a, input_b, expected):
    """Test the division operation."""
    assert division_fixture.calculate(input_a, input_b) == expected

def test_division_by_zero(division_fixture):
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError):
        division_fixture.calculate(5, 0)

@pytest.mark.parametrize("input_a, input_b", [
    (5, "a"),      # Invalid input type
    ("b", 3),      # Invalid input type
    (None, 4),     # NoneType input
])
def test_addition_invalid(addition_fixture, input_a, input_b):
    """Test addition operation raises TypeError for invalid inputs."""
    with pytest.raises(TypeError):
        addition_fixture.calculate(input_a, input_b)

@pytest.mark.parametrize("input_a, input_b", [
    (5, "a"),      # Invalid input type
    ("b", 3),      # Invalid input type
    (None, 4),     # NoneType input
])
def test_subtraction_invalid(subtraction_fixture, input_a, input_b):
    """Test subtraction operation raises TypeError for invalid inputs."""
    with pytest.raises(TypeError):
        subtraction_fixture.calculate(input_a, input_b)

@pytest.mark.parametrize("input_a, input_b", [
    (3, "a"),      # Invalid input type
    ("b", 3),      # Invalid input type
    (None, 4),     # NoneType input
])
def test_multiplication_invalid(multiplication_fixture, input_a, input_b):
    """Test multiplication operation raises TypeError for invalid inputs."""
    with pytest.raises(TypeError):
        multiplication_fixture.calculate(input_a, input_b)

@pytest.mark.parametrize("input_a, input_b", [
    (5, "a"),      # Invalid input type
    ("b", 5),      # Invalid input type
    (None, 5),     # NoneType input
])
def test_division_invalid(division_fixture, input_a, input_b):
    """Test division operation raises TypeError for invalid inputs."""
    with pytest.raises(TypeError):
        division_fixture.calculate(input_a, input_b)
