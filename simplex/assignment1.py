import sys
from equation import Equation
from sdictionary import Dictionary

def buildDictionaryFromFile(inputData):
    datalines = inputData.split('\n')
    lines = []
    for line in datalines:
        lines.append(line.split())

    
    basicCount= int(lines[0][0])
    nbasicCount= int(lines[0][1])
    
    equations = []
    nonBasicVars = map(int,lines[2])
    
    for basic in range(0,basicCount):
        basicVar = lines[1][basic]
        bValue = lines[3][basic]
        rhsMap = {} 
        count =0 
        for key in nonBasicVars:
            rhsMap[key] = float(lines[4+basic][count])
            count+=1
            
        eq = Equation(basicVar,float(bValue),rhsMap)
        equations.append(eq)
    
    lastline = lines[4+basicCount]
    
    rhsMap = {}
    count = 0
    zValue = float(lastline[0])
    for key in nonBasicVars:
        rhsMap[key] = float(lastline[1+count])
        count+=1
        
    objective = Equation(0,zValue,rhsMap)
    
    sdict = Dictionary(equations,objective)

    entry = sdict.getBlandsRuleVar()
    print entry
    leaving = sdict.getLeavingVar(entry)
    if leaving is None:
        print "Unbounded"
    else:
        print leaving
    sdict.pivotDictionary(entry,leaving)
    
    if leaving is not None:
        print sdict.objective.bValue
    else:
        print "n/a"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        buildDictionaryFromFile(inputData)
    else:
        print 'input file are missing'

