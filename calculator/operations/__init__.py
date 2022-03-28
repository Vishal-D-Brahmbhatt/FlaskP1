""" These are the Operation Classes"""
'''value_1,value_2'''

class Addition:
    """ This is the addition class"""

    # this defines a static method that you can use without instantiating the calculator class
    # If you can go to the store and buy it, it is an an object.  If you can't buy it then its a static method
    @staticmethod
    def add(inp1, inp2):
        """ This is the add method"""
        return inp1 + inp2


class Subtraction:
    """ This is the subtraction class"""

    @staticmethod
    def subtract(inp1, inp2):
        """ This is the subtract method"""
        return inp1 - inp2


class Multiplication:
    """ This is the Multiplication class"""

    @staticmethod
    def multiply(inp1, inp2):
        """ This is the multiply method"""
        return inp1 * inp2

class Division:
    """ This is the Division class"""

    @staticmethod
    def divide(cal_tuple_list: tuple):
        """ This is the divide method"""
        return cal_tuple_list[0] / cal_tuple_list[1]
