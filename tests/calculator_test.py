"""Testing the Calculator"""
# From specifies the namespace
from calculator import Calculator


def test_calculator_add_method():
    """Testing the Calculator"""
    # this is show using the calculator object add method
    cal_tuple_list = (8, 4)
    assert Calculator.add(cal_tuple_list) == 12


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    cal_tuple_list = (8, 4)
    assert Calculator.subtract(cal_tuple_list) == -12


def test_calculator_multiply_method():
    """Testing the Calculator Subtract"""
    cal_tuple_list = (8, 4)
    assert Calculator.multiply(cal_tuple_list) == 32


def test_calculator_divide_method():
    """Testing the Calculator Subtract"""
    cal_tuple_list = (8, 4)
    assert Calculator.divide(cal_tuple_list) == 2
