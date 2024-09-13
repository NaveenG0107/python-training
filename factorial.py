inputValue = int(input("Enter a number:"))

def factorialMethodOne(inputVal):
    factorialValue = 1
    if(inputVal == 0):
        return 1
    else:
        while(inputVal>0):
              factorialValue *= inputVal
              inputVal -= 1
    return factorialValue
print("The factorial value for first method:%d" %factorialMethodOne(inputValue))

                                    ##### method2 #####

def factorialMethodTwo(inputVal):
     if(inputVal == 0 or inputVal ==1):
          return 1
     else:
           factorialValue = inputVal * factorialMethodTwo(inputVal - 1)
           return factorialValue
print("The factorial value for second method:%d" %factorialMethodTwo(inputValue))