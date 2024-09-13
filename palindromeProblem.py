userValue = input("Enter your number:")
userValue = userValue.lower()
result = ""
i = len(userValue)-1
while(i>=0):
    result = result + userValue[i]
    i -= 1
print("Your reverse value is %s" %result)
if(userValue == result):
    print("Your value %s is palindrome" %result)
else:
    print("Your value %s is not a palindrome" %result)

                                    ##### method2 #####
userValue = input("enter your value:")
userValue = userValue.lower()
i=0
result =""
while(i<len(userValue)):
    if(userValue[i] == userValue[len(userValue)-i-1]):
        result += userValue[i]
    i += 1
if(userValue == result):
    print("Your value %s is palindrome" %result)
else:
    print("Your value %s is not a palindrome" %result)


                                     #####  method3 #####
userValue = input("enter the value:")
result= ""
for i in userValue:
    result = i+result
if(userValue == result):
    print("Your value %s is palindrome" %result)
else:
    print("Your value %s is not a palindrome" %result)
