
userInput = input("Enter your string:")
def stringPositionOne(userInp):
    result = ""
    for i in userInput:
        if(i == "#"):
            result = i + result
        else:
            result = result + i
    return result 
print("The alternative result is:",stringPositionOne(userInput))

                                    ##### method 2 #####
userInput = input("enter the string:")
def stringPositionTwo(userInput):
    sortValue = ""
    count = 0
    result =""
    for i in userInput:
        if(i == "#"):
            sortValue = sortValue +""
            count += 1
        else:
            sortValue = sortValue + i
    for i in range(count):
        result += "#"
    return result + sortValue  
print(stringPositionTwo(userInput))

                                    ##### method 3 #####

userInput = input("Enter the string:")
def stringPositionThree(userInput,sortValue ="",result=""):
    for i in userInput:
        if(i == "#"):
            result = result + "#"
        else:
            sortValue = sortValue + i
    print(result + sortValue)  
stringPositionThree(userInput)
 
                                    ##### method 4 #####
  
def stringPositionFour(userInput, selectChar ="#"):
    selectCharLength = len(selectChar)
    startValue = ""
    endValue = ""
    i = 0
    while (i <len(userInput)):
        if userInput[i:i+ selectCharLength] == selectChar:
            startValue += selectChar
            i += selectCharLength
        else:
            endValue += userInput[i]
            i += 1
    return startValue + endValue

userInput= input("enter the string:")
print(stringPositionFour(userInput)) 



           



