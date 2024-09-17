
def convertInteger(romanValue):
    if (romanValue == "I" or romanValue =="i"):
        return 1
    elif(romanValue == "V" or romanValue =="v"):
        return 5
    elif(romanValue == "X" or romanValue == "x"):
        return 10
    elif(romanValue == "L" or romanValue == "l"):
        return 50
    elif(romanValue == "C" or romanValue == "c"):
        return 100
    elif(romanValue == "D" or romanValue == "d"):
        return 500
    elif(romanValue == "M" or romanValue == "m"):
        return 1000
    else:
        return -1

def romanToInt(userInput):
    i=0
    result = 0
    while(i < len(userInput)):
        value1 = convertInteger(userInput[i]) 
        if(i+1<len(userInput)):
            value2 = convertInteger(userInput[i+1])
            if(value1>=value2):
                result += value1
                i +=1
            else:
                result += value2 -value1
                i +=2 
        else:
            result += value1
            i +=1 
    return result


userInput = input("Enter roman characters:")
print("The roman value is:",romanToInt(userInput))