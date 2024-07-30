# BASIC NUMBER GUESSER GAME
import random

print("Welcome to the Number Guesser Game!")

max_bound = input("What maximum value till you want to guess? ")
if max_bound.isdigit():
    max_bound = int(max_bound)
    if max_bound <= 0:
        print("Please enter a number greater than 0 next time.")
        quit()
else:
    print("Please enter a number next time!")
    quit()

random_number = random.randint(0, max_bound)
#print(random_number)

chance = 0
while True:
    chance += 1
    user_choice = int(input(f"Choose a number between 1 to {max_bound}: "))
    if user_choice == random_number:
        print("You got it right!")
        break
    elif user_choice > random_number:
        print("You guessed a larger number, Guess again!")
    else:
        print("You guessed a smaller number, Guess again!")

# print("You took " + str(chance) + " chance to guess the number!")
# print("You took", chance, "chance to guess the number!")
print(f"You took {chance} chance to guess the number!")