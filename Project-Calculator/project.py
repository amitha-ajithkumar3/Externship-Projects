

choice = int(input("Welcome to Error-free calculator! Choose an option: 1. Addition 2. Subtraction 3. Multiplication 4.Division 5.Exit: "))
result = 0

def addition(num, num1):
    return num + num1

def subtraction(num, num1):
    return num - num1
    
def multiplication(num, num1):
  return num * num1
    
def division (num, num1):
   return num/num1
 

while choice != 5:
    if choice == 1:
        try:
            num = int(input(f"Enter the first number: "))
            num1 = int(input(f"Enter the second number: "))
        except ValueError:
            print("Invalid value")
        else:
            print(f"The result is {addition(num, num1)}")
   
    elif choice == 2:
        try:
            num = int(input(f"Enter the first number: "))
            num1 = int(input(f"Enter the second number: "))
        except ValueError:
            print("Invalid value")
        else:
            print(f"The result is {subtraction(num, num1)}")

    elif choice == 3:
        try:
            num = int(input(f"Enter the first number: "))
            num1 = int(input(f"Enter the second number: "))
        except ValueError:
            print("Invalid value")
        except ZeroDivisionError:
            print("Number cannot be divided by 0")
        else:
            print(f"The result is {multiplication(num, num1)}")

    elif choice == 4:
        try:
            num = int(input(f"Enter the first number: "))
            num1 = int(input(f"Enter the second number: "))
        except ValueError:
            print("Invalid value")
        else:
            print(f"The result is {division(num, num1)}")

    elif choice == 5:
        print("Thanks for using the calculator!")
        break
    choice = int(input("Try again: 1. Addition 2. Subtraction 3. Multiplication 4.Division 5.Exit: "))

  
