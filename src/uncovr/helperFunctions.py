#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Invoke Libraries
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
from pandas import DataFrame, concat
from numpy import transpose
from logging import error

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Functions
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#Handles missing arguments by replacing with the default values
def missingArgHandler(argMissed,argDefault):
    
    return argDefault if argMissed is None else argMissed


#Generates alpha numeric sequences
def alphaNumericSeq(noOfItems, prefix):
    alphanumSeq = [prefix + str(i) for i in range(1, noOfItems+1)]
    return alphanumSeq

#Error and status code to user friendly messages
def errorCodeHandler(self):
    statusLookUp = {401:'Please check if you have the passed the correct subscription key. If problem persists, please raise an issue at https://github.com/FoyiLabs/uncovr-python',
                    500: 'There seems to an error on server side. Please try again. If problem persists, please raise an issue at https://github.com/FoyiLabs/uncovr-python'
                   }
    msg = (statusLookUp.get(self))
    if msg is not None:
        error(msg)
    return

#Extract df function 
def extractDf(self):
    depVarRaw = self.json()["depVar"]
    depVarDf = DataFrame({'dv':depVarRaw})
    indepVarRaw = self.json()["indepVars"]
    noOfIvs = len(indepVarRaw)
    ivNames = alphaNumericSeq(noOfItems = noOfIvs, prefix = "iv")
    indepVarDf = DataFrame(transpose(indepVarRaw), columns = ivNames)    
    outDf = concat([depVarDf, indepVarDf.reset_index(drop=True) ], axis=1)
    
    return outDf