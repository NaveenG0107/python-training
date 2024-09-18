def findSquareOne(userInput):
    for i in range(0,userInput):
        if(i*i ==userInput):
            return True 
    else:
            return False 
def findSquareTwo(userInput):
    for i in range(1,userInput):
        if((userInput/i)/i == 1):
            return True 
    else:
            return False    
        
userInput = int(input("Enter the positive number:"))
if(userInput > 0):
    print(findSquareOne(userInput))
    print(findSquareTwo(userInput))
else:
    print("Please enter positive integer")


