# implementation of card game - Memory

import simplegui
import random

exposed = ["False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False"]
list1 = range(8)
list2 = range(8)
game_list = list1 + list2
letter_pos = 50
width = 50
height = 100
turn_counter = 0
state = 0
flipped1 = 0
flipped2 = 0
exposed1 = 0
exposed2 = 0


# helper function to initialize globals
def new_game():
    global game_list, exposed, turn_counter, state
    random.shuffle(game_list)
    turn_counter = 0
    label.set_text("Turns = " + str(turn_counter))
    state = 0
    exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, flipped1 , flipped2, exposed1, exposed2, turn_counter
    flipped_cards = []   
    if state == 0:
        card_click = pos[0] // 50  
        flipped1 = game_list[card_click]
        #print flipped1
        flipped_cards.append(card_click)
        exposed[card_click] = True
        exposed1 = int(card_click)
        #print exposed1
        #print flipped_cards
        state = 1
    elif state == 1:
        card_click = pos[0] // 50
        if exposed[card_click] == False:
            exposed[card_click] = True
            flipped2 = game_list[card_click]
            #print flipped2
            flipped_cards.append(card_click)
            #print flipped_cards
            exposed[card_click] = True
            exposed2 = int(card_click)
            #print exposed2
            turn_counter += 1
            label.set_text("Turns = " + str(turn_counter))
            #print turn_counter
            state = 2
            
    else:
        card_click = pos[0] // 50
        if exposed[card_click] == False:
                exposed[card_click] = True
                if flipped1 != flipped2:
                    exposed[exposed1] = False
                if flipped1 != flipped2:
                    exposed[exposed2] = False
                    #print exposed
                flipped1 = game_list[card_click]
                #print flipped1
                flipped_cards.append(card_click)
                exposed[card_click] = True
                exposed1 = int(card_click)
                #print exposed1
                #print flipped_cards
                state = 1           
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global letter_pos, game_list, exposed
    for card_index in range(len(game_list)):
        card_pos = 50 * (card_index + 0.5)
        if exposed[card_index] == False:
            canvas.draw_line(([25 + 50 * card_index, 0]), (25 + 50 * card_index, 100), 49, "Green",)
        else:    
            canvas.draw_text(str(game_list[card_index]), (card_pos, 50), 24, "White")
        

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns =" + str(turn_counter))


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
