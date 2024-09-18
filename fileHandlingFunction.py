fileValue = open("fileHandlingValue.txt", "r")
fetchValue = fileValue.readlines()
fileValue.close()
stringValue = ""
result = ""
for i in fetchValue:
    stringValue +=str(i)
i = len(stringValue)-1
while(i>=0):
    result = result + stringValue[i]
    i -= 1
fileWrite = open("fileHandlingValue.txt", "w")
fileWrite.write(result)
fileWrite.close()
file = open("fileHandlingValue.txt","r")
print(file.readline())

                                    ##### append method #####

fileValue = open("fileHandlingValue.txt", "r")
fetchValue = fileValue.readlines()
fileValue.close()

fileValue = open("fileHandlingValue.txt", "w")
fileValue.write("")
fileValue.close()

stringValue = ""
result = ""
for i in fetchValue:
    stringValue +=str(i)
i = len(stringValue)-1
while(i>=0):
    result = result + stringValue[i]
    i -= 1
fileWrite = open("fileHandlingValue.txt", "a")
fileWrite.write(result)
fileWrite.close()
file = open("fileHandlingValue.txt","r")
print(file.readline())