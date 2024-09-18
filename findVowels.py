userInput = input("Enter a string:")

def findVowelsOne(userInput):
    count = 0
    for i in userInput:
        if (i == "a" or i== "e" or i == "i" or i == "o" or i == "u"):
            count +=1
        elif(i == "A" or i== "E" or i == "I" or i == "O" or i == "U"):
            count +=1
    return count

def findVowelsTwo(userInput):
    count = 0
    list =['a','e','i','o','u','A','E','I','O','U']
    for i in userInput:
        if i in list:
            count +=1
    return count                             
print("The vowels present in the input:",findVowelsOne(userInput))
print("The vowels present in the input:",findVowelsTwo(userInput))


