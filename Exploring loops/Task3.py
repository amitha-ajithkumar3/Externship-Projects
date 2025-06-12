user_input= int(input("Enter a number: "))
j=user_input
count = 1

for i in range (1, user_input+1):
    count = count*i


print(f"The factorial of {j} is = {count}", end = "")


