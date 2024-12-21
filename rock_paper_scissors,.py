import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's and computer's choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def main():
    """Main function to play the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions: Enter 'rock', 'paper', or 'scissors' to play. Enter 'quit' to exit.")

    while True:
        user_choice = input("Your choice (rock/paper/scissors): ").lower()

        if user_choice == "quit":
            print("Thanks for playing!")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            print(f"Final Score: You {user_score} - {computer_score} Computer")
            break

if __name__ == "__main__":
    main()
