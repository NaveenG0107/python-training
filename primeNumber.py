userInput = int(input("Enter the number:"))

def primeMethodOne(inputVal):
    for value in range(2,inputVal):
        result = 1
        i = 2
        while(i<value):
            if (value % i == 0):
                result = 0
                i = value +1
            i += 1
        if result == 1:
            print (value)
    return "They are all prime numbers"
print(primeMethodOne(userInput))

                                    ##### method2 #####
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, (num//2) + 1):
        if num % i == 0:
            return False
    return True
result = []
for num in range(1, userInput):
    if is_prime(num):
        result = result +[num]
print(result)



