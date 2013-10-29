from equation import Equation

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

    def allLeavingVars(self,enteringKey):
        
        valueDict = {}
        for equation in self.basicEquations:
           
            value = equation.valueOfEntry(enteringKey)
            
            if value >= float(0):
               valueDict[equation.basicVar] = value    
         
        if len(valueDict.keys()) == 0:
            #dictionay is unbounded
            self.unbounded = True
            return None
        
        return valueDict

    def getLeavingVar(self,enteringKey):
        valueDict = self.allLeavingVars(enteringKey)
        if valueDict is None:
            return None 

        return min(valueDict.items(), key=lambda x: x[1])[0]
    
    def pivotDictionary(self,enterVar,leavingVar):
            
        if self.unbounded == True or self.final == True:
            return False
        
        if leavingVar == None:
            return False

        #find the leavingVar equtation
        leavingEquation = None

        for equation in self.basicEquations:
            if equation.basicVar == leavingVar:
                leavingEquation = equation
        
        if equation is None:
            return False
        
        leavingEquation.exitVarRebalance(enterVar)

        for equation in self.basicEquations:
            if equation.basicVar != leavingEquation.basicVar:
                equation.substituteEquation(leavingEquation)
        
        self.objective.substituteEquation(leavingEquation)
        
        return True
        
