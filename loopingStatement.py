               ##### for loop #####
userList = ["rahul", " ", "surya", "sanjay"]
for i in userList:
    if(i != " "):
        print("hii"+ " "+ i +" "+ "Welcome to our site")
    else:
        print("Enter valid name")
        continue

               ##### while loop ##### 

userInput = [10, 3, 13, 44]
i = 0
max = 0
while(i< len(userInput)):
    if(max < userInput[i]):
        max = userInput[i]
    i += 1
print("Maximum number is:",max)

    