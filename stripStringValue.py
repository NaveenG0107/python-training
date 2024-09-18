userInput =  [2,4,[3,5,[1,[9]]],0]
result =[]
def listJoin(userInput,result):
    for i in userInput:
        if type(i) == list: 
            listJoin(i,result)
        else:
            result +=[i]
    return result
print(listJoin(userInput,result))

                                      ##### method 2 #####
userInput =  [2,4,[3,5,[1,[9]]],0]
list =[]
result =[]
for i in userInput:
    i = str(i)
    for val in i:
        if val == "[" or val =="]":
            pass
        else:
            list +=[val]
for i in list:
    if (i ==" " or i == ","):
        pass
    else:
        result += i
print(result)                    