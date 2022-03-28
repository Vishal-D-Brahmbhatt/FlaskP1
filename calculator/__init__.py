""" This is the Calculator Class"""
from calculator.calculations import Addition, Subtraction, Multiplication, Division


class Calculator:
    """ This is the default result property"""

    @staticmethod
    def add(cal_tuple_list):
        """ This is the add method"""
        # Call the static method add to return the sum and set it to the calculator result property
        calculation = Addition.create(cal_tuple_list)
        return calculation.get_result()

    @staticmethod
    def subtract(cal_tuple_list):
        """ This is the subtract method"""
        calculation = Subtraction.create(cal_tuple_list)
        return calculation.get_result()

    @staticmethod
    def multiply(cal_tuple_list):
        """ This is the subtract method"""
        calculation = Multiplication.create(cal_tuple_list)
        return calculation.get_result()

    @staticmethod
    def divide(cal_tuple_list):
        """ This is the subtract method"""
        calculation = Division.create(cal_tuple_list)
        return calculation.get_result()
