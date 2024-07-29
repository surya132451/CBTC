import random

def get_alpha_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_beta_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        choice = input("Invalid choice. Enter rock, paper, or scissors: ").lower()
    return choice

def determine_winner(beta, alpha):
    if beta == alpha:
        return "It's a tie!"
    elif (beta == "rock" and alpha == "scissors") or \
         (beta == "paper" and alpha == "rock") or \
         (beta == "scissors" and alpha == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        beta = get_beta_choice()
        alpha = get_alpha_choice()
        print(f"You chose: {beta}")
        print(f"Computer chose: {alpha}")
        result = determine_winner(beta, alpha)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()

