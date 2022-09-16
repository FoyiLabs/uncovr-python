#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Invoke Libraries
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
from requests import post
from json import dumps


#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Function
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#Set lookup values
apiEndPoint = "https://foyi.azure-api.net/uncovr/uncovr/"


# Function to call uncovr API
def uncovrApi(body, key, params):
    headers =  {"Content-Type":"application/json", "Ocp-Apim-Subscription-Key" : key}    
    response = post(apiEndPoint, params = params, data = dumps(body), headers=headers)
    return response