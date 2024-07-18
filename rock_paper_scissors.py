import random
choices = ["rock", "paper", "scissors"]

def who_wins(user_choice, computer_choice):
  if user_choice == computer_choice:
    return " Game Tie"
  
  elif user_choice == "rock":
    if computer_choice == "scissors":
      return "Win"
    else:
      return "Lose"
    
  elif user_choice == "paper":
    if computer_choice == "rock":
      return "Win"
    else:
      return "Lose"
    
  elif user_choice == "scissors":
    if computer_choice == "paper":
      return "Win"
    else:
      return "Lose"
  else:
    return "Invalid choice"
  
user_score = 0
computer_score = 0

while True:
  print("Welcome to Rock-Paper-Scissors!")
  print("Choose rock, paper, or scissors (or 'q' to quit):")

  user_choice = input("> ").lower()

  if user_choice == 'q':
    break
  if user_choice not in choices:
    print("Invalid choice. Please try again.")
    continue

  computer_choice = random.choice(choices)
  print(f"You chose: {user_choice}")
  print(f"Computer chose: {computer_choice}")
  result = who_wins(user_choice, computer_choice)
  if result == "Win":
    print("You win!")
    user_score += 1 
  elif result == "Lose":
    print("You lose!")
    computer_score += 1 
  else:
    print("It's a tie!")

  if user_score or computer_score:
    print(f"Current score: You - {user_score}, Computer - {computer_score}")

  play_again = input("Play again? (y/n): ").lower()
  if play_again != 'y':
    break

print("Thanks for playing!")

