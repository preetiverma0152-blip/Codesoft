import random

def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock-Paper-Scissors Game!")
    print("Instructions: Type rock, paper, or scissors to play.\n")

    while True:
        # User Input
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("⚠ Invalid choice! Please choose rock, paper, or scissors.")
            continue

        # Computer Selection
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Display Choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Game Logic
        if user_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round!")
            computer_score += 1

        # Score Tracking
        print(f"Score → You: {user_score} | Computer: {computer_score}\n")

        # Play Again?
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n🏆 Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing! 👋")
            break


# Run the game
play_game()
