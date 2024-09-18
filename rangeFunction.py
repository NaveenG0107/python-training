def rangeFunction(startValue = None, length = None, increment = None ):
    if(startValue != None and length ==None and increment == None):
        list =[]
        length = 0
        increment =1
        while(startValue > length):
            list +=[length]
            length +=increment
        return tuple( list)
    elif(startValue != None and length !=None and increment ==None):
        list =[]
        increment =1
        while(startValue < length):
            list +=[startValue]
            startValue += increment
        return tuple( list)
    else:
        list =[]
        if (startValue < length and increment >0):
            while(startValue < length):
                list +=[startValue]
                startValue += increment
            return tuple( list)
        elif(startValue >length and increment <0):
            while(startValue > length):
                list +=[startValue]
                startValue += increment
            return tuple (list)
                                    ##### method 1 #####

def rangeFunctionTwo(startValue = 0, length =0 ,increment =1):
    list =[]
    if (startValue < length and increment >0):
        while(startValue < length):
            list +=[startValue]
            startValue += increment
        return tuple( list)
    elif(startValue >length and increment <0):
        while(startValue > length):
            list +=[startValue]
            startValue += increment
        return tuple (list)
    elif(startValue >length and increment > 0):
        while(startValue > length):
            list +=[length]
            length +=increment
        return tuple( list)
                
print(rangeFunction(0,10))
for i in rangeFunctionTwo(10):
    print(i)
        


