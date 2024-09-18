def reverseMethodOne(userInput):
    result = 0
    while(userInput > 0):
        reminder = userInput % 10
        result = (result*10) + reminder
        userInput = userInput //10
    return result

def reverseMethodTwo(userInput):
    stringValue = str(userInput)
    result = ""
    for i in stringValue:
        result = i + result
    return int(result)

def reverseMethodThree(userInput):
    stringValue = str(userInput)
    result = stringValue[::-1]
    return int(result)

userInput = int(input("Enter a valid integer:"))
print(reverseMethodOne(userInput))
print(reverseMethodTwo(userInput))
print(reverseMethodThree(userInput))
