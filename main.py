def get_choices():
    player_choice = input("select a choice either rock, paper or scissors")
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}

    return choices


choices = get_choices()
print(choices)
