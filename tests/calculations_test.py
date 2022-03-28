"""Testing the Calculator"""
# From specifies the namespace
from calculator.calculations import Addition, Subtraction, Multiplication, Division


def test_calculation_multiplication_instance():
    """Testing the Calculator Subtract"""
    cal_tuple_list = (8, 4) #ARRANGE
    calculation = Multiplication.create(cal_tuple_list) #ACT
    assert isinstance(calculation, Multiplication) #ASSERT


def test_calculation_division_instance():
    """Testing the Calculator Divide"""
    cal_tuple_list = (8, 4) #ARRANGE
    calculation = Division.create(cal_tuple_list) #ACT
    assert isinstance(calculation, Division) #ASSERT

def test_calculation_subtraction_instance():
    """Testing the Calculator Subtract"""
    cal_tuple_list = (8, 4) #ARRANGE
    calculation = Subtraction.create(cal_tuple_list) #ACT
    assert isinstance(calculation, Subtraction) #ASSERT

def test_calculation_addition_instance():
    """Testing the Calculator Subtract"""
    cal_tuple_list = (8, 4) #ARRANGE
    calculation = Addition.create(cal_tuple_list) #ACT
    assert isinstance(calculation, Addition) #ASSERT


def test_calculation_add_get_result_method():
    """Testing the Calculator"""
    # this is show using the calculator object add method
    cal_tuple_list = (8, 4)
    calculation = Addition.create(cal_tuple_list)
    assert calculation.get_result() == 12


def test_calculation_subtract_get_result_method():
    """Testing the Calculator Subtract"""
    cal_tuple_list = (8, 4) #ARRANGE
    calculation = Subtraction.create(cal_tuple_list) #ACT
    assert calculation.get_result() == -12 #ASSERT


def test_calculation_multiply_get_result_method():
    """Testing the Calculator Subtract"""
    cal_tuple_list = (8, 4) #ARRANGE
    calculation = Multiplication.create(cal_tuple_list) #ACT
    assert calculation.get_result() == 32 #ASSERT

def test_calculation_divide_get_result_method():
    """Testing the Calculator Divide"""
    cal_tuple_list = (8, 4) #ARRANGE
    calculation = Division.create(cal_tuple_list) #ACT
    assert calculation.get_result() == 2 #ASSERT
