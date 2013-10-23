import unittest

class EquationTestClass(unittest.TestCase):

    def setUp(self):
        self.equation = Equation(1,4.6,{2:-5.7,3:5.7}) 

    def test_equation(self):
        self.assertIsNotNone(self.equation)
    
    def test_value_for_entering_var(self):
        equation = Equation(1,4.0,{2:-2.0,3:2.0})
        self.assertEquals(equation.value_for_entering_var(2),2.0)
        self.assertEquals(equation.value_for_entering_var(3),-2.0)

class Equation(object):
    
    def __init__(self,basicVar,bValue,rhsDict):
        self.basicVar = basicVar
        self.bValue = bValue
        self.rhsDict = dict(rhsDict)
        
    def value_for_entering_var(self,enterIndex):
        coeffValue = self.rhsDict[enterIndex]
        value = float(self.bValue)/float(-coeffValue)  
        return value
