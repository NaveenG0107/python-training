userInput = input("Enter a value with commas:")
def sumSplitValuesOne(userInput):
    sum = 0
    listValue =[]
    for i in userInput:
        if(i != ","):
            sum += int(i)
        elif(i == ","):
            listValue += [sum]
            sum =0
    listValue += [sum]
    return listValue

def sumSplitValuesTwo(userInput):
    listValue = []
    lastSum = 0
    for i in range(0,len(userInput)):
        if (userInput[i] == ","):
            sum = 0
            for num in range(i-1,-1, -1):    
                if(userInput[num] == ","):
                    break
                else:
                    sum += int(userInput[num])
            listValue +=[sum]
        elif(i == len(userInput)-1):
            for num in range(i,0,-1):
                if(userInput[num] != ","):
                    lastSum += int(userInput[num]) 
                else:
                    break
    return listValue + [lastSum]
print(sumSplitValuesOne(userInput))
print(sumSplitValuesTwo(userInput))