def factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

def fibonacci (x):
    if x == 0:
        return 0
    elif x ==1:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)

print(factorial(5))
num = 7
print(f" The {num}th number of the fibonacci sequence is {fibonacci(num)}")

