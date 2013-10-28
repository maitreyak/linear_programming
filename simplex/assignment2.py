#This file invokes and prints expected results related to assigment 2
import sys
import file_to_dict_script as script
from equation import Equation
from sdictionary import Dictionary

def pivotToFinal(sdict):
    if sdict.final == True:
        #dict is alread a final one
        print sdict.objective.bValue
        print str(0)
    
    pivotCounts = 0
    
    while sdict.final != True:
        entry = sdict.getBlandsRuleVar()
        
        if sdict.final == True:
            #dict is alread a final one
            print sdict.objective.bValue
            print str(pivotCounts)
            return
        
        leaving = sdict.getLeavingVar(entry)
        
        if sdict.unbounded == True:
            print "UNBOUNDED"
            return

        sdict.pivotDictionary(entry,leaving)
        pivotCounts+=1

    return
        

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        sdict = script.buildDictionaryFromFile(fileLocation)
        if sdict is not None:
            pivotToFinal(sdict)
        else:
            print "Something is a miss here"
