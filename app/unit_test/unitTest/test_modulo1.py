import unittest
from packagePython.my_package import modulo1

class TestModulo1(unittest.TestCase):
    def test_add(self):
        self.assertEqual(modulo1.add(2,2), 4)
    
    def test_substract(self):
        self.assertEqual(modulo1.substract(2,2), 0)

unittest.main()
    