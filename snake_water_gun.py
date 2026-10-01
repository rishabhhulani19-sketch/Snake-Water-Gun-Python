import random


def play_round(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (
        (player_choice == "snake" and computer_choice == "water")
        or (player_choice == "water" and computer_choice == "gun")
        or (player_choice == "gun" and computer_choice == "snake")
    ):
        return "player"
    else:
        return "computer"


choices = ["snake", "water", "gun"]
player_score = 0
computer_score = 0
rounds_played = 0
max_rounds = 3

print("Let's play Snake Water Gun!")
print(f"The game will run for {max_rounds} rounds.")

while rounds_played < max_rounds:
    print(f"\n--- Round {rounds_played + 1} ---")

    # Get player's choice
    while True:
        player_input = input(
            "Enter your choice (snake, water, gun): "
        ).lower()

        if player_input in choices:
            player_choice = player_input
            break
        else:
            print(
                "Invalid choice. Please choose from "
                "'snake', 'water', or 'gun'."
            )

    # Get computer's choice
    computer_choice = random.choice(choices)

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine winner of the round
    winner = play_round(player_choice, computer_choice)

    if winner == "player":
        player_score += 1
        print("You won this round!")
    elif winner == "computer":
        computer_score += 1
        print("Computer won this round!")
    else:
        print("It's a tie!")

    print(f"Score: You {player_score} - Computer {computer_score}")
    rounds_played += 1

print("\n--- Game Over ---")

if player_score > computer_score:
    print(
        f"Congratulations! You won the game "
        f"{player_score} to {computer_score}!"
    )
elif computer_score > player_score:
    print(
        f"Too bad! Computer won the game "
        f"{computer_score} to {player_score}."
    )
else:
    print(
        f"It's a tie game! Final score: "
        f"You {player_score} - Computer {computer_score}."
    )
