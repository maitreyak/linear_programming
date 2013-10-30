#This file invokes and prints expected results related to assigment 3
import sys
import file_to_dict_script as script
from equation import Equation
from sdictionary import Dictionary
from idictionary import InitializationDictionary

def initPivotToFinal(sdict):
    if sdict.final == True:
        #dict is alread a final one
        print sdict.objective.bValue
    
    
#    printDictionary(sdict) 
    sdict.forcePivot()
 #   printDictionary(sdict)

    while sdict.final != True:
        entry = sdict.getBlandsRuleVar()
        if sdict.final == True:
            #dict is alread a final one
            print round(sdict.objective.bValue,3)
            return
        
        leaving = sdict.getLeavingVar(entry)
        
        if sdict.unbounded == True:
            print "UNBOUNDED"
            return

        sdict.pivotDictionary(entry,leaving)
  #      printDictionary(sdict)
    return


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
        initDict = InitializationDictionary(sdict)
        if initDict is not None:
            initPivotToFinal(initDict)    
        else:
            print "Something is a miss here"
