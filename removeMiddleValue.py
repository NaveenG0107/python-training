
                                    ##### method 1 #####
listLength = int(input("Enter the list length:"))
list =[]
result = []
for i in range(0,listLength):
    listValue = input(f"Enter the {i+1} value:")
    list += [listValue]
if(len(list)%2 ==0):
    fmiddle = len(list)//2
    smiddle = len(list)//2 -1
    for i in range(0,len(list)):
        if(i == fmiddle or i == smiddle):
            pass
        else:
            result +=[list[i]] 
else:
    middle = len(list)//2
    for i in range(0,len(list)):
        if(i == middle):
            pass
        else:
            result +=[list[i]]
print(result)

                                    ##### method 2 #####

listLength = int(input("Enter the list length:"))
list =[]
decrement =1
result = []
for i in range(0,listLength):
    listValue = input(f"Enter the {i+1} value:")
    list += [listValue]
if(len(list)%2 !=0):
    for i in range(0,len(list)):
        j= len(list) - decrement
        if i == j:
            pass
        else:
            if list[i] in result:
                pass
            else:
                result += [list[i]]
        decrement +=1
    print(result)
else:
    ivalue =[]
    jvalue =[]
    for i in range(0,len(list)):
        j = len(list) - decrement
        if(i<j):
            ivalue +=[list[i]]
            jvalue +=[list[j]]
            
        else:
            pass
        decrement +=1
    for i in range(0,len(ivalue)-1):
        result +=[ivalue[i]]
    for j in range(len(jvalue)-2,-1,-1):
        result +=[jvalue[j]]
    print(result) 
