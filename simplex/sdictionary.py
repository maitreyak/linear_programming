from equation import Equation
import math

class Dictionary(object):
    
    def __init__(self,basicEquations,objective):
        self.basicEquations = basicEquations
        self.objective = objective
        self.final = False
        self.unbounded = False
        self.allInterger = False
    
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

    def maxOfVariableIndex(self):
        eq = max(self.basicEquations, key=lambda x: x.basicVar)
        obj = max(self.objective.rhsDict.keys())
        if (int(eq.basicVar) > int(obj)): 
            return (int(eq.basicVar)) 
        else:
            return (int(obj))
    
    
    def addCuttingPlanes(self):
        self.allInterger = True
        cuttingPlains = []
        count = 1
        for equation in self.basicEquations:
            diff = float(str(equation.bValue - float(math.floor(equation.bValue)))) 
            if (diff != float(0)):
                self.allInterger = False
                newEquation = Equation(self.maxOfVariableIndex()+count,diff,{})
                count +=1
                for key in equation.rhsDict:
                    newEquation.rhsDict[key] = float(str(equation.rhsDict[key] - float(math.floor(equation.rhsDict[key]))))     
                    
                cuttingPlains.append(newEquation)
                
        for newEq in cuttingPlains:
            self.basicEquations.append(newEq)

    def getDualDictionary(self):
        newEquations = []
        
        newObjective = Equation(0,-self.objective.bValue,{})
        
        for key in self.objective.rhsDict:
            
            if(self.objective.rhsDict[key] != float(0)):
                newBvalue= -self.objective.rhsDict[key]
            else:
                newBvalue= 0.0
                
            newEquations.append(Equation(int(key),newBvalue,{}))
        
        for eq in self.basicEquations:
            for newEq in newEquations:
                if newEq.basicVar in eq.rhsDict:
                    if eq.rhsDict[newEq.basicVar] != float(0):
                        newEq.rhsDict[eq.basicVar] = -eq.rhsDict[newEq.basicVar]        
                    else:
                        newEq.rhsDict[eq.basicVar] = 0.0
            
            if(eq.bValue != float(0)):
                newObjective.rhsDict[eq.basicVar] = -eq.bValue
            else:
                newObjective.rhsDict[eq.basicVar] = 0.0

        dualDict = Dictionary(newEquations,newObjective)
        return dualDict
          
            
        
         
        
