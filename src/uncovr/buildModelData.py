#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Invoke Libraries
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
from helperFunctions import missingArgHandler
from uncovrApi import uncovrApi
from indepAndDep import indepAndDep


#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Function
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def model2data(numOfObs=None, numOfVars=None, key=None):
    #Error handling
    if key is None:
        print("Error: Please pass subscription key in the function.")
        return

    #Impute missing arguments
    numOfObs = missingArgHandler(argMissed = numOfObs, argDefault = 1000)
    numOfVars = missingArgHandler(argMissed = numOfVars, argDefault = 10)

    #Call out out of bound errors
    if(numOfObs < 100 or numOfObs > 10000):
      print("Error: numOfObs must be atleast 100 and not more than 10,000.")
      return
    
    if(numOfVars < 1 or numOfVars > 100):
      print("Error: numOfVars must be atleast 1 and not more than 100.")
      return
    
    #Source independent and dependent variable attributes in a json format needed for uncovr api
    body = indepAndDep(numOfObs = numOfObs, numOfVars = numOfVars)

    #Call the api and source the response
    resp = uncovrApi(body = body, key = key)

    #Error handling
    responseCode = resp.status_code
    if (responseCode == 401):
      print("Error: please check if you have entered the correct subscription key. If problem persists, please raise an issue at https://github.com/FoyiLabs/uncovr-python")
    #need to work on this. Convert the json output to a dataframe for the user and return dataframe

    return
