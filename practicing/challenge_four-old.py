import unittest

from challenge4.Fibonacci import *
from challenge4.ConvertToString import *

class challenge4(unittest.TestCase):

    def test_operators_functions(self):

        # Get order
        order = input("Enter Fibonacci series order(integer) : ")
        try:
            order = int(order)
        except ValueError:
            assert False, "Invalid input, please enter a number > 0"

        # Get Fibonacci number
        fibonacci_number = Fibonacci.get_fibonacci()

        # Covert to string
        number_sentence = ConvertToString.get_number_sentence(fibonacci_number)
        print("---------OUTPUT-----------")
        print(str(fibonacci_number) + " - " + str(number_sentence))


if __name__ == '__main__':
    unittest.main()