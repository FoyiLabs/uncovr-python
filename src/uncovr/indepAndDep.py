

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Invoke Libraries
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
from numpy import random
from json import dumps
from uncovr.helperFunctions import alphaNumericSeq

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Function
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def indepAndDep(numOfObs, numOfVars):
    #Since this is a internal function, no error handling is made.
    
    #Build outer list scaffolding    
    ivNames = alphaNumericSeq(noOfItems = numOfVars, prefix = "iv")

    #Iterate over the idependent variables and create their attributes
    allIvDict = {}    

    for iv in ivNames:
        allIvDict[iv] = {}
        #Upper and lower bound ranges are currently hardcoded. This could be given out as parameter in later versions
        upperBound = random.uniform(0.01, 100)
        lowerBound = -1*upperBound   
        allIvDict[iv]["noOfpoints"] = numOfObs
        allIvDict[iv]["upperBound"] = upperBound
        allIvDict[iv]["lowerBound"] = lowerBound
        allIvDict[iv]["dataType"] = "continuous"

    #Build dependent variable attributes. Currently there is only one.
    dvDict = {} 
    dvDict["dataType"] = "continuous"

    #Build a combo dictionary of dependent and independent variables
    comboDict = {}
    comboDict["iv"] = allIvDict
    comboDict["dv"] = dvDict 

    return comboDict

