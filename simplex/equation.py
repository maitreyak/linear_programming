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
        
        newBValue= subEquation.bValue * replaceNonBasicCoeff
        self.bValue += newBValue
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

    def equals(equation1,equation2):
        if (equation1.basicVar !=  equation2.basicVar) or (equation1.bValue != equation2.bValue):
            return False

        for key in equation1.rhsDict.keys():
            
            if equation1.rhsDict[key] == float(0):
                if key in equation2.rhsDict and equation2.rhsDict[key] != float(0):
                    return False
                else:
                    continue    

            if key not in equation2.rhsDict:
                return False
            if equation1.rhsDict[key] != equation2.rhsDict[key]:
                return False
           
        return True

    def copy(self):
        copy = Equation(self.basicVar,self.bValue,self.rhsDict)
        return copy 

