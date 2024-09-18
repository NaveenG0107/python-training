listLength = int(input("Enter the list length:"))
list =[]
for i in range(0,listLength):
    listValue = int(input(f"Enter the {i+1} value:"))
    list += [listValue]
def sortingFunctionOne(list, length = len(list)):
    for i in range(length-1):
        for j in range(length-1):
            if(list[j] > list[j+1]):
                swap = list[j]
                list[j] = list[j+1]
                list[j+1] = swap
    return list
def sortingFunctionTwo(list,length = len(list)):
    if length==1:
        return list
    for i in range(length-1):
        if(list[i] > list[i+1]):
            swap = list[i]
            list[i] = list[i+1]
            list[i+1] = swap
    return sortingFunctionTwo(list ,length-1)
print(sortingFunctionOne(list))
print(sortingFunctionTwo(list))


                                    