

from symbol import pass_stmt


def LeapYear(x):
    if (x<0):                #Now check if user input is a positive number
        return False
    elif (x % 4== 0) and (x % 100 != 0): #conditions for leap year updated
        print(x, "is a leap year")
        return True
    elif (x % 400 == 0):
        print(x, "is a leap year")
        return True
    else:
        print(x, "is not a leap year")
        return False
        

def FizzBuzz():
    for i in range(1,100,1):
        if (i%3==0 and i%5==0):
            print("FizzBuzz")
            return "FizzBuzz"
        elif (i%3==0):
            print("Fizz")
            return "Fizz"
        elif (i%5==0):
            print("Buzz")
            return "Buzz"
        else:
            pass



    



