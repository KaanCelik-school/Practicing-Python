def WantedInput():
    while True:
        try:
            x = int(input("please enter x: "))
            y = int(input("please enter y: "))
            return x, y
        except ValueError:
            print ("Please enter a valid number")
            exit()
def Addition(x, y):
    return x + y
    
def Subtraction(x, y):
    return x - y
    
def Multiplication(x, y):
    return x * y

def Division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        exit()
    
def Choice(x, y):
    while True:
        try:
            choice = int(input("Which operation would you like to do? 1 for addition, 2 for multiplication, 3 for subtraction and 4 for division: "))
            if choice == 1:
                return Addition(x, y)
            elif choice == 2:
                return Multiplication(x, y)
            elif choice == 3:
                return Subtraction(x ,y)
            elif choice == 4:
                return Division(x, y)
            else: 
                print("invalid choice")
                return None
        except ValueError:
            print ("Enter a valid choice")

x, y= WantedInput()
result = Choice(x, y)
if result is not None:
    print("Result is:", result)

    
