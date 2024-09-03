import random

def generate_number(min_val=1, max_val=100):
    return random.randint(min_val, max_val)

def check_guess(number, guess):
    if guess < number:
        return "Too low!"
    elif guess > number:
        return "Too high!"
    else:
        return "Correct!"

def play_game(max_attempts=4, min_val=1, max_val=100):
    number = generate_number(min_val, max_val)
    attempts = 0

    print(f"Guess the number between {min_val} and {max_val}!")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            result = check_guess(number, guess)
            print(result)
            attempts += 1

            if result == "Correct!":
                return True

        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Sorry, you've used all your attempts. The number was {number}.")
    return False
