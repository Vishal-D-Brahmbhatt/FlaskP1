"""Testing the calculator operations """

from calculator.operations import Addition, Subtraction, Multiplication, Division


def test_calculator_operations_add():
    """Testing the Calculator"""
    assert Addition.add(8, 4) == 12


def test_calculator_operations_subtract():
    """Testing the Calculator"""
    assert Subtraction.subtract(1, 1) == 0


def test_calculator_operations_multiply():
    """Testing the Calculator"""
    assert Multiplication.multiply(8, 4) == 32


def test_calculator_operations_divide():
    """Testing the Calculator"""
    cal_test = (8, 4)
    assert Division.divide(cal_test) == 2
