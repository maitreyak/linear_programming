from equation import Equation
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
            
    #def test_getLeavingVar(self):
    #    self.sdict


class Dictionary(object):
    
    def __init__(self,basicEquations,objective):
        self.basicEquations = basicEquations
        self.objective = objective
        self.final = False
        self.unbounded = False
    
    def getEnteringVars(self):
        #Just look for positve coeffs
        entryVar = []
        for key in self.objective.rhsDict.keys():
            if self.objective.rhsDict[key] > float(0):
                entryVar.append(key)
        
        if len(entryVar) == 0:
            #the dict is final
            self.final = True        
        
        return entryVar
    
    def getBlandsRuleVar(self):
        
        if self.final == True:
            return None
        
        entryVars = self.getEnteringVars()
        
        if len(entryVars) == 0:
            return None
        
        #apply blands rule
        return min(entryVars)

    def getLeavingVar(self,enteringKey):
        return None     


