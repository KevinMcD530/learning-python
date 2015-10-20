# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

# initialize global variables used in your code here
num_range = 100
secret_number = random.randrange(0, 100)
guess_counter = int(7)

# helper function to start and restart the game
def new_game():
    global secret_number
    global num_range
    num_range = int(num_range)
    secret_number = random.randrange(0,num_range)
    return secret_number
    global counter
    return counter
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    new_game()
    global num_range
    num_range = 100
    secret_number = random.randrange(0,num_range)
    print " "
    print "New Game. The number is between 0 - 100, you have", guess_counter, "guesses"   
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    new_game()
    global num_range
    num_range = 1000
    global counter
    counter = int(10)
    global secret_number
    secret_number = random.randrange(0,num_range)
    global guess_counter
    guess_counter = 10
    print " "
    print "New Game. The number is between 0 - 1000, you have", guess_counter,"guesses"  
    pass

 

def input_guess(guess):
    # main game logic goes here	
    guess = int(guess)
    global num_range
    global guess_counter
    print " "
    #print "Number of remaining guess is %d." % chances
    print "Guess was", guess
    guess_counter = guess_counter - 1
    print "Number of remaining guesses is", guess_counter
    if guess_counter == 0:
        print "You have run out of guesses, a new game will now start"
        new_game()
        if num_range == 100:
            range100()
        else:
            range1000()          
    if guess > secret_number:
        print "Lower!"
        return guess
    elif guess < secret_number:
        print "Higher!"
        return guess
    elif guess == secret_number:
        print "Correct!"
        new_game()
        if num_range == 100:
            guess_counter = 7
            range100()
        else:
            guess_counter = 10
            range1000()
    else:
        print "You lose!"
        
       
    
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements and start frame
button_100 = frame.add_button('Range is [0, 100)', range100)
button_1000 = frame.add_button('Range is [0, 1000)', range1000)
guess_box = frame.add_input("Enter a Guess", input_guess, 100)


# call new_game 

frame.start()
new_game()
range100()

# always remember to check your completed program against the grading rubric
