for i in range (1,51,1):
    num = i
    if (num % 3 ==0):
        print (str(num) + " Fizz")
    elif (num % 5 == 0):
        print (str(num) + " Buzz")
    elif (num % 3 == 0 and num% 5 == 0):
        print (str(num) +" FizzBuzz")
    else:
        print (str(num)+" No es múltiplo de ni de 3, ni de 5 ni de ambos")
