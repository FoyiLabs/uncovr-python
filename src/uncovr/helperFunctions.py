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

#Need to work: Error and status code to user friendly messages

#Need to work: extract df function 