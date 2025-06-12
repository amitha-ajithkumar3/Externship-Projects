import turtle

choice = int(input("Welcome to the Recursive Artistry Program! Choose an option: 1. Calculate Factorial 2. Find Fibonacci 3. Exit: "))

while choice != 4 and choice>0:
    if choice == 1:
        def factorial (n):
            if n == 0 or n == 1:
             return 1
            else:
                 return n*factorial(n-1)
            
        num = int(input(f"Enter a number to find its factorial: "))
        print(f" The factorial of {num} is {factorial(num)}")
        break
    
    elif choice == 2:
        def fibonacci (x):
            if x == 0:
                return 0
            elif x ==1:
                return 1
            else:
                return fibonacci(x-2)+fibonacci(x-1)
            
        num1 = int(input(f"Enter the position of the Fibonaccis number: "))
        print(f" The {num1}th number of the fibonacci series is {fibonacci(num1)}")
    
    else:
        print("Invalid Input")
        break
    choice = int(input("Choose another option: 1. Calculate Factorial 2. Find Fibonacci 3. Draw a Recursive Fractal 4. Exit: "))

  