userData = int(input("Enter the value:"))
def moduloMethod(userData):
    if(userData%2 ==0):
        print(str(userData) + " " + "is even")
    else:
        print(str(userData) + " " + "is odd")
                                    ##### method 2 #####
def floorMethod(userData):
    if((userData //2)*2 == userData):
        print(str(userData) + " " + "is even")
    else:
        print(str(userData) + " " + "is odd")

moduloMethod(userData)
floorMethod(userData)
