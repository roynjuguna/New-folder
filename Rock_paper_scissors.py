import random
def get_choice():
    my_choice = input(" enter a choice(rock, paper, scissors): ")
    random_options= ["rock", "paper", "scissors"]
    computer_choice = random.choice(random_options)
    choices = {"player": my_choice, "computer": computer_choice}

    return choices 

def check_win(player, computer):
    print (f"player chose {player} , computer chose {computer}")
    if player == computer:
        return " its a tie"
    elif player == "rock":
        if computer =="scissors":
            return "rock crushes scissors, you win!"
        else:
            return "paper covers rock, you lose."
        
    elif player == "paper":
        if computer =="rock":
            return "rock covers paper, you win."
        else:
            return "scissors cuts paper, you lose."

    elif player == "scissors":
        if computer =="paper":
            return "scissors cuts paper, you win!"
        else:
            return "rock crushes scissors, you lose."
    
choices = get_choice()

result = check_win(choices["player"], choices["computer"])
print (result)

print("First ever game")
    
    
    



