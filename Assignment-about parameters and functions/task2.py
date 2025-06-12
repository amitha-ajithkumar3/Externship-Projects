def describe_pet(pet_name, animal_type = "dog"):
    print(f"I have a {animal_type} named {pet_name}.")

name_choice = input("Enter a pet name ")
animal_choice=input("Enter an animal type ")
describe_pet(name_choice, animal_choice)

