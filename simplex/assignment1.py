#This file invokes and prints expected results related to assigment 1
import sys
import file_to_dict_script as script
from equation import Equation
from sdictionary import Dictionary

def pivotOnce(sdict):
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
        sdict = script.buildDictionaryFromFile(fileLocation)
        if sdict is not None:
            pivotOnce(sdict)
        else:
            print "Something is a miss here"
