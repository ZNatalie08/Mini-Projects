import random

def get_choices():
    player_choice = input("Enter a choice (rock/paper/scissors): ")
    while player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
        move = input("Enter one of the three options: rock, paper, scissors \n Your choice: ")
        player_choice = move
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, your opponent chose {computer}.")
    if player == computer:
        return "It's a tie !"
    elif player == "rock":
        if computer == "scissors":
            return "You won :)"
        else:
            return "You lost :("
    elif player == "paper":
        if computer == "scissors":
            return "You lost :("
        else:
            return "You won :)"
    elif player == "scissors":
        if computer == "paper":
            return "You won :)"
        else:
            return "You lost :("


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)



