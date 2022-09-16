#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Invoke Libraries
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
from uncovr.helperFunctions import missingArgHandler, errorCodeHandler
from uncovr.uncovrApi import uncovrApi
from uncovr.indepAndDep import indepAndDep
from logging import error


#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Function
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def model2data(numOfObs=None, numOfVars=None, key=None):
    #Error handling
    if key is None:
        error("Please pass subscription key in the function.")
        return

    #Impute missing arguments
    numOfObs = missingArgHandler(argMissed = numOfObs, argDefault = 1000)
    numOfVars = missingArgHandler(argMissed = numOfVars, argDefault = 10)

    #Call out out of bound errors
    if(numOfObs < 100 or numOfObs > 10000):
      error("numOfObs must be atleast 100 and not more than 10,000.")
      return
    
    if(numOfVars < 1 or numOfVars > 100):
      error("numOfVars must be atleast 1 and not more than 100.")
      return
    
    #Source independent and dependent variable attributes in a json format needed for uncovr api
    body = indepAndDep(numOfObs = numOfObs, numOfVars = numOfVars)

    #Call the api and source the response
    params = {"funcName" : "indepAndDep"}
    resp = uncovrApi(body = body, params = params, key = key)

    #If there is a known error, handle it with meanigful and non technical messages. Provide an action if the issue persists.
    responseCode = resp.status_code
    errorCodeHandler(responseCode)   

    return resp
