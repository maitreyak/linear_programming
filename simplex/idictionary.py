from equation import Equation
from sdictionary import Dictionary

class InitializationDictionary(Dictionary):
    def __init__(self,dictionary):
        self.basicEquations = []
        self.final = False
        self.unbounded = False

        for eq in dictionary.basicEquations:
            auxEq = eq.copy()
            auxEq.rhsDict[-1]=1.0
            self.basicEquations.append(auxEq)    
        self.objective= Equation(0,0.0,{-1:1.0})
        leavingEquation= min(self.basicEquations,key=lambda x: x.bValue)
        self.pivotDictionary(-1,leavingEquation.basicVar)        
            
    
        

