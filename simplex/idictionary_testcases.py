from equation import Equation
from sdictionary import Dictionary
from idictionary import InitializationDictionary
import unittest

class DictionaryTestCase(unittest.TestCase):
        
    def setUp(self):        
       self.basicEquations = []
       self.basicEquations.append(Equation(1,1.0,{2:0.0,4:0.0,5:-1.0,7:-2.0}))
       self.basicEquations.append(Equation(3,3.0,{2:1.0,4:-1.0,5:0.0,7:-1.0}))
       self.basicEquations.append(Equation(6,0.0,{2:-1.0,4:0.0,5:-2.0,7:0.0}))
       self.objective= Equation(0,1.0,{2:-1.0,4:2.0,5:3.0,7:1.0})
       self.sdict = Dictionary(self.basicEquations,self.objective)
       self.initDict = InitializationDictionary(self.sdict)

    def test_initDictionary(self):
        self.assertIsNotNone(InitializationDictionary(self.sdict))
        
    def test_forceEnteringVar(self):
        self.assertEquals(self.initDict.forceEnteringVar(),-1)
    
    def test_forceLeavingVar(self):
        self.assertEquals(self.initDict.forceLevaingVar(),6)

    def test_forcePivot(self):
        self.assertTrue(self.initDict.forcePivot())

