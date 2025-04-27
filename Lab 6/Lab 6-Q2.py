import random

class Rock_paper_scissors:
    def __init__(self, total_rounds):
        self.total_rounds = total_rounds
        self.current_round = 1
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ["rock", "paper", "scissors"]

    def get_computer_choice(self):
        return random.choice(self.choices)

    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "draw"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.user_wins += 1
            return "user"
        else:
            self.computer_wins += 1
            return "computer"

    def check_winner(self):
        if self.user_wins > self.total_rounds // 2:
            return "User wins the game!"
        elif self.computer_wins > self.total_rounds // 2:
            return "Computer wins the game!"
        return None

    def play_game(self):
        print(f"\nStarting Rock-Paper-Scissors! Best of {self.total_rounds} rounds.")

        while self.current_round <= self.total_rounds:
            print(f"\nRound {self.current_round}")
            user_choice = input("Choose rock, paper, or scissors: ").lower()

            if user_choice not in self.choices:
                print("Invalid choice. Try again.")
                continue

            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")

            result = self.find_winner(user_choice, computer_choice)

            if result == "draw":
                print("It's a draw!")
            elif result == "user":
                print("You win this round!")
            else:
                print("Computer wins this round!")

            game_winner = self.check_winner()
            if game_winner:
                print("\n" + game_winner)
                break  # Stop the game early if someone wins

            self.current_round += 1

        print(f"\nFinal Score - You: {self.user_wins} | Computer: {self.computer_wins}")
        if self.user_wins == self.computer_wins:
            print("It's a tie game!")


while True:
    try:
        rounds = int(input("Enter the number of rounds: "))
        if rounds <= 0:
            print("Please enter a positive number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

game = Rock_paper_scissors(rounds)
game.play_game()
