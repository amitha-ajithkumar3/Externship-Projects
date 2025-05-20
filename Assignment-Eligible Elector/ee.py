user_age = int(input("Enter your age: "))

if user_age>=18: #checks if age is greater than 18
    print("You can now vote! Congrats!") #positive message when user is eligbile

elif user_age<18 and user_age>=0: #checks if age is lesser than 18
    print("Sorry, you cannot vote yet, but you only have ", 18-user_age, " years left till you can!")  #printing number of years left until user can vote


else: #setting condition for invalid/string inputs
    print("Invalid input, try again")
