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
        self.objective= Equation(0,0.0,{-1:-1.0})
    
    def forceLevaingVar(self):
        leavingEquation= min(self.basicEquations,key=lambda x: x.bValue)
        return leavingEquation.basicVar

    def forceEnteringVar(self):
        return -1

    def forcePivot(self):
        return self.pivotDictionary(self.forceEnteringVar(),self.forceLevaingVar())
    

