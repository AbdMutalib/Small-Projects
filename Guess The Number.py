import random
secret_number = random.randint(1, 9)
guess_count_choice = 0
guess_count_choice_tries = 0
guess_count_choice_tries_message = ["What is wrong with you", "Can't you read", "Dude, come on", "You crazy, mahn"]

# guess count
guess_count_choice = int(input("How many times would you like to guess (1-5) : ")) - 1

while guess_count_choice < 1 or guess_count_choice > 4:
    print("You can only guess 1 - 5 time(s) ")
    guess_count_choice_tries += 1
    guess_count_choice = int(input("How many time would you like to guess (1 - 5) : ")) - 1

    if guess_count_choice_tries > 2:
        print(random.choice(guess_count_choice_tries_message))

# guessing
guess = int(input("Guess The Secret Number From 1-9 : "))
while guess:
    print(f"The number is not {guess}")
    if guess < secret_number:
        print("Ishhh, Higher")
    elif guess > secret_number:
        print("Ishhh, Lower")
    guess_count_choice -= 1
    guess = int(input("Try Again! : "))

    if guess == secret_number:
        print(f"Correct!!! {guess} is the secret number")
        break

    elif guess == secret_number and guess_count_choice == 0:
        print(f"Correct!!! {guess} is the secret number")
        break

    elif guess_count_choice == 0:
        print("You failed, you failure :) ")
        print(f"The number was {secret_number}")
        break


