import unittest

from challenge4.fibonacci_sequence import *
from challenge4.number_to_word import *

class challenge4(unittest.TestCase):

    def test_functions(self):
        # Invoke fibonacci_sequence script
        get_fibonacci = fibonacci(n)
        # print(get_fibonacci)

        # Pass get_fibonacci result to number_to_word script
        num = get_fibonacci
        get_words = convert(num)
        # print(get_words)
        print(str(get_fibonacci) + " - " + get_words)

if __name__ == '__main__':
    unittest.main()

