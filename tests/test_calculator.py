import pytest
from src.calculator import Calculator

@pytest.fixture
def calc():
    """Fixture to provide a Calculator instance."""
    return Calculator()

def test_add(calc):
    assert calc.add(1, 2) == 3
    assert calc.add(-1, 1) == 0

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(2, 5) == -3

def test_multiply(calc):
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6

def test_divide(calc):
    assert calc.divide(6, 2) == 3
    assert calc.divide(5, 2) == 2.5

def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(1, 0)

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (10, -5, 5),
    (0, 0, 0)
])
def test_add_parameterized(calc, a, b, expected):
    assert calc.add(a, b) == expected
