from equation import Equation
from sdictionary import Dictionary
import unittest

class DictionaryTestCase(unittest.TestCase):

    def setUp(self):
        self.basicEquations = []
        self.basicEquations.append(Equation(1,4.0,{3:2.0,4:-3.0,2:1.0,7:1.0}))
        self.basicEquations.append(Equation(5,5.0,{3:0.0,4:3.0,2:-1.0,7:-2.0}))
        self.basicEquations.append(Equation(6,0.0,{3:0.0,4:-1.0,2:1.0,7:3.0}))
        self.objective= Equation(0,10.0,{3:-1.0,4:1.0,2:-1.0,7:0.0})
        self.sdict = Dictionary(self.basicEquations,self.objective)
    
    def test_dictionarySetup(self):
        test_sdict = Dictionary(self.basicEquations,self.objective)
        self.assertIsNotNone(test_sdict)

    def test_getEnteringVars(self):
        self.assertIsNotNone(self.sdict.getEnteringVars())

    def test_getEnteringCountAndIndexAndNotFinal(self):
        # we know there is only one entering var 
        self.sdict.objective = Equation(0,10.0,{3:-1.0,4:1.0,2:-1.0,7:0.0})
        self.assertEquals(len(self.sdict.getEnteringVars()),1) 
        self.assertEquals(self.sdict.getEnteringVars()[0],4)
        self.assertFalse(self.sdict.final)

    def test_getEnteringZeroCountAndFinal(self):
        #we now chnage the dict's objective to be final
        self.sdict.objective = Equation(0,10.0,{3:-1.0,4:0.0,2:-1.0,7:0.0})
        self.assertEquals(len(self.sdict.getEnteringVars()),0) 
        self.assertTrue(self.sdict.final)

    def test_blandsRule(self):
        #we know for the default dict in the test case the index is 4
        self.assertEquals(self.sdict.getBlandsRuleVar(),4)

    def test_blandsRuleMutiple(self):
        self.sdict.objective = Equation(0,10.0,{3:-1.0,4:1.0,2:1.0,7:0.0})
        self.assertEquals(len(self.sdict.getEnteringVars()),2) 
        self.assertEquals(self.sdict.getBlandsRuleVar(),2)
            
    def test_getLeavingVar(self):
        basicEquations = []
        basicEquations.append(Equation(1,1.0,{2:0.0,4:0.0,5:-1.0,7:-2.0}))
        basicEquations.append(Equation(3,3.0,{2:1.0,4:-1.0,5:0.0,7:-1.0}))
        basicEquations.append(Equation(6,0.0,{2:-1.0,4:0.0,5:-2.0,7:0.0}))
        objective= Equation(0,1.0,{2:-1.0,4:2.0,5:3.0,7:1.0})
        sdict = Dictionary(basicEquations,objective)

        self.assertEquals(sdict.getLeavingVar(4),3)
    
    def test_getLeavingVarUnbounded(self):
        basicEquations = []
        basicEquations.append(Equation(1,4.0,{3:2.0,4:3.0,2:1.0,7:1.0}))
        basicEquations.append(Equation(5,5.0,{3:0.0,4:3.0,2:-1.0,7:-2.0}))
        basicEquations.append(Equation(6,5.0,{3:0.0,4:1.0,2:1.0,7:3.0}))
        objective= Equation(0,10.0,{3:-1.0,4:1.0,2:-1.0,7:0.0})
        sdict = Dictionary(basicEquations,objective)
        self.assertIsNone(sdict.getLeavingVar(sdict.getBlandsRuleVar()))
        self.assertTrue(sdict.unbounded)

    def test_pivotDictionary(self):
       # 3 4
       # 1 3 6
       # 2 4 5 7
       # 1 3 0
       # 0 0 -1 -2
       # 1 -1 0 -1
       # -1 0 -2 0
       # 1 -1  2 3 1
        basicEquations = []
        basicEquations.append(Equation(1,1.0,{2:0.0,4:0.0,5:-1.0,7:-2.0}))
        basicEquations.append(Equation(3,3.0,{2:1.0,4:-1.0,5:0.0,7:-1.0}))
        basicEquations.append(Equation(6,0.0,{2:-1.0,4:0.0,5:-2.0,7:0.0}))
        objective= Equation(0,1.0,{2:-1.0,4:2.0,5:3.0,7:1.0})
        sdict = Dictionary(basicEquations,objective)
        
        enter = sdict.getBlandsRuleVar()
        exit = sdict.getLeavingVar(enter)
        self.assertEquals(enter,4)
        self.assertEquals(exit,3)
        self.assertTrue(sdict.pivotDictionary(enter,exit))
        self.assertEquals(sdict.objective.bValue,7.0)

    def test_maxOfVariableIndexys(self):
        self.assertEquals(self.sdict.maxOfVariableIndex(),7)

    def test_addCuttingPLanes(self):
        basicEquations = []
        basicEquations.append(Equation(1,1.2,{2:0.4,4:0.0,5:-1.4,7:-2.0}))
        basicEquations.append(Equation(3,3.4,{2:1.1,4:-1.1,5:0.0,7:-1.0}))
        basicEquations.append(Equation(6,0.0,{2:-1.0,4:0.0,5:-2.0,7:0.0}))
        objective= Equation(0,1.0,{2:-1.0,4:2.0,5:3.0,7:1.0})
        sdict = Dictionary(basicEquations,objective)
        sdict.addCuttingPlanes()
        self.assertEquals(len(sdict.basicEquations),5)
        
        for eq in sdict.basicEquations:
            if(eq.basicVar == 8):
                self.assertTrue(eq.equals(Equation(8,0.2,{2:0.4,4:0.0,5:0.6,7:0.0})))
            if(eq.basicVar == 9):
                self.assertTrue(eq.equals(Equation(9,0.4,{2:0.1,4:0.9,5:0.0,7:0.0})))

    def test_getDualDictionary(self):
        dual = self.sdict.getDualDictionary()
        self.assertEquals(len(dual.basicEquations),4)
        self.assertTrue(dual.objective.equals(Equation(0,-10.0,{1:-4.0,5:-5.0,6:0.0})))

        for eq in dual.basicEquations:
            if eq.basicVar == 7:
                self.assertTrue(eq.equals(Equation(7,0.0,{1:-1.0,5:2.0,6:-3.0})))


                

