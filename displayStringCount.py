                                        #####method 1 ######
userInput = input("Enter a text:")
result = {} 
for char in userInput:
 if char in result: 
  result[char] += 1
 else:
  result[char] = 1 
for value in result:
 print(str(value)+str(result[value]), end = "")

                                    ##### method 2 #####
userInput = input("Enter some text with multiple character:")  
count = [None] * len(userInput) ; 
for i in range(0, len(userInput)):  
    count[i] = 1;  
    for j in range(i+1, len(userInput)):  
        if(userInput[i] == userInput[j]):  
            count[i] = count[i] + 1;    
            userInput = userInput[ : j] +"0" + userInput[j+1 : ];         
for i in range(0, len(count)):  
    if(userInput[i] != ' ' and userInput[i] != '0'):  
        print(userInput[i] + str(count[i]), end="")  

                                    ##### method 3 #####
user_input = input("Enter a string: ")

unique_chars = ""

frequencies = []

for char in user_input:
    found = False
    for u in unique_chars:
        if u == char:
            found = True
            break
    if not found:
        unique_chars += char
        count = 0
        for c in user_input:
            if c == char:
                count += 1
        frequencies.append(count)

for i in range(len(unique_chars)):
    print(str(unique_chars[i])+str(frequencies[i]), end = "")
    
    
