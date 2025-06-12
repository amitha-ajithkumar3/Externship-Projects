try:
    num = int(input("Enter a number to check: "))
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Number cannot be divided by 0")
