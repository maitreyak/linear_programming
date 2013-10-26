from equation import Equation
import unittest

class EquationTestCase(unittest.TestCase):

    def setUp(self):
        self.equation = Equation(1,4.6,{2:-5.7,3:5.7}) 

    def test_equation(self):
        self.assertIsNotNone(self.equation)
    
    def test_valueOfEntry(self):
        equation = Equation(1,4.0,{2:-2.0,3:2.0})
        self.assertEquals(equation.valueOfEntry(2),2.0)
        self.assertEquals(equation.valueOfEntry(3),-2.0)
    
    def test_valueOfEntryInvalidEntry(self):
        self.assertIsNone(self.equation.valueOfEntry(9))
         
    def test_valueOfEntryZeroCoeff(self):
        self.equation.rhsDict[10] = 0.0
        self.assertIsNone(self.equation.valueOfEntry(10))
     
    def test_exitVarRebalanceInvalidIndex(self):
        self.assertFalse(self.equation.exitVarRebalance(103))

    def test_exitVarRebalanceInvalidCoeff(self):
        self.equation.rhsDict[103] = 0.0
        self.assertFalse(self.equation.exitVarRebalance(103))
    
    def test_exitVarRebalance(self):
        equation = Equation(1,4.0,{2:-2.0,3:2.0})
        self.assertTrue(equation.exitVarRebalance(2))
        self.assertEquals(equation.basicVar,2)
        self.assertEquals(equation.bValue,2.0)
        self.assertEquals(equation.rhsDict[1],-0.5)
        self.assertEquals(equation.rhsDict[3],1.0)
        self.assertFalse(equation.exitVarRebalance(2))

    def test_substituteEquationNone(self):
        self.assertFalse(self.equation.substituteEquation(None))
    
    def test_substituteEquationZeroCoeff(self):
        equation1 = Equation(1,4.0,{2:-2.0,3:2.0})
        equation2 = Equation(4,4.0,{1:0.0,3:2.0})
        self.assertTrue(equation2.substituteEquation(equation1)) 

    def test_substituteEquation(self):
        equation1 = Equation(1,4.0,{2:-2.0,3:2.0})
        equation2 = Equation(4,4.0,{1:-2.0,3:2.0})
        self.assertTrue(equation2.substituteEquation(equation1))   
        self.assertEquals(equation2.basicVar,4)
        self.assertEquals(equation2.bValue,-4.0)
        self.assertEquals(equation2.rhsDict[2],4.0)
        self.assertEquals(equation2.rhsDict[3],-2.0)
        self.assertEquals(len(equation2.rhsDict.keys()),2)

    def test_equationEqualsTrue(self):
        self.assertTrue(Equation.equals(Equation(1,4.0,{2:-2.0,3:2.0}),Equation(1,4.0,{2:-2.0,3:2.0})))
        self.assertTrue(Equation.equals(Equation(1,4.0,{3:2.0}),Equation(1,4.0,{3:2.0})))
        self.assertTrue(Equation.equals(Equation(1,4.0,{4:0.0,3:2.0}),Equation(1,4.0,{3:2.0})))

    def test_equationEqualsFalse(self):
        self.assertFalse(Equation.equals(Equation(1,4.0,{6:-2.0,3:2.0}),Equation(1,4.0,{2:-2.0,3:2.0})))
        self.assertFalse(Equation.equals(Equation(1,4.0,{2:0.0,3:2.0}),Equation(1,4.0,{2:-2.0,3:2.0})))
