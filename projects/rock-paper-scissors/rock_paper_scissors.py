import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'user'
    else:
        return 'computer'

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    user_score = 0
    computer_score = 0
    rounds = int(input("How many rounds would you like to play? "))

    for _ in range(rounds):
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == 'user':
            print("You win this round!")
            user_score += 1
        elif winner == 'computer':
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("This round is a draw!")

        print(f"Scores => You: {user_score} | Computer: {computer_score}")
    
    if user_score > computer_score:
        print(f"Congratulations! You won the game with a score of {user_score} to {computer_score}.")
    elif user_score < computer_score:
        print(f"Sorry, you lost the game. Final score is You: {user_score} | Computer: {computer_score}.")
    else:
        print(f"The game is a draw with both scoring {user_score}.")

if __name__ == "__main__":
    play_game()
