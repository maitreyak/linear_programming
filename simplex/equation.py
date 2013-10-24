class Equation(object):
    
    def __init__(self,basicVar,bValue,rhsDict):
        self.basicVar = basicVar
        self.bValue = bValue
        self.rhsDict = dict(rhsDict)
        
    def valueOfEntry(self,enterIndex):
        if enterIndex not in self.rhsDict:
            return None
        
        coeffValue = self.rhsDict[enterIndex]
        
        if coeffValue == float(0):
            return None
        
        value = float(self.bValue)/float(-coeffValue)  
        return value
    
    def exitVarRebalance(self,varIndex): 
        if varIndex not in self.rhsDict:
            return False
        
        coeffValue = float(self.rhsDict[varIndex])        
        
        if coeffValue == float(0):
            return False
        
        self.rhsDict[self.basicVar] = -1 
        self.basicVar = varIndex
        del self.rhsDict[varIndex]

        for key in self.rhsDict.keys():
            self.rhsDict[key] /= -coeffValue        
        
        self.bValue = self.bValue/-coeffValue
        return True
    
    def substituteEquation(self,subEquation):
        if subEquation is None:
            return False
        
        replaceNonBasic = subEquation.basicVar
        
        if replaceNonBasic not in self.rhsDict:
            return True
        
        replaceNonBasicCoeff = self.rhsDict[replaceNonBasic]
        del self.rhsDict[replaceNonBasic]
        
        if  replaceNonBasicCoeff == float(0):
            return True
        
        subEquation.bValue *= replaceNonBasicCoeff
        self.bValue += subEquation.bValue

        newRhsDict ={}
        
        for key in subEquation.rhsDict.keys():
           newRhsDict[key] = subEquation.rhsDict[key] *replaceNonBasicCoeff
                
        for key in self.rhsDict.keys():
            if key in newRhsDict:
                newRhsDict[key] += self.rhsDict[key]
            else:
                newRhsDict[key] = self.rhsDict[key]
        
        self.rhsDict = newRhsDict
        
        return True

