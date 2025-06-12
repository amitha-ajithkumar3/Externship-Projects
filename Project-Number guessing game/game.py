import random
number_to_guess = random.randint(1, 100)
count = 9
user_input= int(input("Enter a number between 1 and 100 to save the princess! "))
while (count>0):
    if(number_to_guess>user_input):
        print(f"Your guess is too low! You have {count} guesses remaining!")
    elif (number_to_guess<user_input):
        print(f"Your guess is too high! You have {count} guesses remaining!")
    elif(number_to_guess==user_input):
        print(f"Congratulations! You guessed it right! You have saved the princess")
        print(f"You won in {count} attempts")
        break
    else:
        print("Invalid Input")
    user_input= int(input("Enter another number: "))
    count = count-1


