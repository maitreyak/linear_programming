#This file invokes and prints expected results related to assigment 3
import sys
import file_to_dict_script as script
from equation import Equation
from sdictionary import Dictionary

def printObjective(equation):
    eq = str(equation.bValue) + ' '
    for key in equation.rhsDict:
        eq += ' + ('+str(equation.rhsDict[key])+" * "+"x"+str(key)+')'
    
    return eq+';'

def printEq(equation):
    eq = 'x'+str(equation.basicVar)+' = ' + str(equation.bValue) + ' '
    for key in equation.rhsDict:
        eq += ' + ('+str(equation.rhsDict[key])+" * "+"x"+str(key)+')'
    
    return eq +';'
    
def gplsol(sdict):
    #printDictionary(sdict)
    
    for i in range(1,20):
        print 'var x'+str(i)+' integer >=0 ;'

    print 'maximize obj: '+printObjective(sdict.objective)
    
    count = 1
    for equation in sdict.basicEquations:
        print 'c'+str(count)+': '+printEq(equation)
        count+=1
    
    print 'solve;'
    print 'display '+printObjective(sdict.objective)
    print 'end;'
    
#solve; 
#display 0.0  + 1.0 * x1   + 1.0 * x2   -5.0 * x3 ;
 
# end;



def printDictionary(sdict):
    for eq in sdict.basicEquations:
        print eq.basicVar,"=",eq.bValue," ",eq.rhsDict
    print "Objective:"
    print sdict.objective.basicVar,"=",sdict.objective.bValue," ",sdict.objective.rhsDict
    print "--------------------"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        sdict = script.buildDictionaryFromFile(fileLocation)
        if sdict is not None:
            gplsol(sdict)    
        else:
            print "Something is a miss here"
