import pytest
from calculator import Calculator

def test_addition():
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 6

def test_subtraction():
    calc = Calculator()
    result = calc.subtract(5, 3)
    assert result == 2

def test_addition_with_non_integers():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.add("a", 3)

def test_subtract_with_non_integers():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.subtract("a", 1)