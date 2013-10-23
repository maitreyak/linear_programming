import unittest

class EquationTestClass(unittest.TestCase):
    
    def test_equation(self):
        self.assertIsNotNone(Equation([1,2,3,4]))

class Equation(object):
    
    def __init__(self,vector = []):
        self.vector = vector
        
