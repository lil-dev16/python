import random
def get_choices():
    player_choice = input("select a choice either rock, paper or scissors")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "tie!!"
    elif player == "rock":
        if computer == "paper":
            return "You lose, paper covers rock!"
        else:
            return "You win, rock smashes scissors!"
    elif player == "scissors":
        if computer == "paper":
            return "you win, scissors cuts paper"
        else:
            return "you lose, rock crushes scissors"
    elif player == "paper":
        if computer == "rock":
            return "you win, paper covers rock"
        else:
            return "you lose, scissors cuts paper"

choicxs = get_choices()

print(check_win(choicxs["player"], choicxs["computer"]))
