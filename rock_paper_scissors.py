# Rock-paper-scissors-lizard-Spock Project

import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "No matches found!"


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "No matches found!"
    

def rpsls(player_choice): 

    #First line of output
    print ""
    print str("Player chooses" + " " + (player_choice))
    player_number = name_to_number(player_choice)
    
    #Second Line of Output
    comp_number = random.randrange(0 , 5)    
    number_to_name(comp_number)
    print str("Computer chooses"),number_to_name(comp_number)
    
    #Who wins the game check and print
    result = (comp_number - player_number) % 5
    if result == 1 or result == 2:
        print "Computer Wins!"
    elif result == 3 or result == 4:
        print "Player Wins!"
    else:
        print "Player and Computer tie!"
    
    
 
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


