# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
dealer_hand = []
my_hand = []
play_deck = []
hand_loc_x = 100
hand_loc_y = 400

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []
        self.hand_value = 0
        pass	

    def __str__(self):
        # return a string representation of a hand
        s = "Hand Contains "
        for i in range(len(self.cards)):
            s += str(self.cards[i]) + " "           
        return s
        

    def add_card(self, card):
    # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        self.hand_value = 0
        for card in self.cards:
            rank = card.get_rank()
            self.hand_value = self.hand_value + VALUES[rank]
        for card in self.cards:
            rank = card.get_rank()
            if rank == 'A' and self.hand_value <= 11:
                self.hand_value += 10

        return self.hand_value              
   
    def draw(self, canvas, pos):
        
        #draw a hand on the canvas, use the draw method for cards
        num_card = 50
        for i in range(len(self.cards)):
            self.cards[i].draw(canvas,[(hand_loc_x * i), 450])
            #hand_loc_x += 100
            
        #for card in self.cards:
            #if card.pos[1] == 450:
                #c.draw(canvas, (pos[0], 450)
                #pos += 50
            #else:
                #c.draw(canvas, (pos[0], 200)
                #pos += 50
             
            
        
class Deck:
    def __init__(self):
        global deck_cards
        self.deck_cards = []
        for suit in SUITS:
            for rank in  RANKS:
                self.deck_cards.append(Card(suit, rank))
        #self.deck_cards = self.deck_cards [ : ]


    def shuffle(self):
        # shuffle the deck 
        
        random.shuffle(self.deck_cards)

    def deal_card(self):
        # deal a card object from the deck
        
        self.dealt_card = self.deck_cards[-1]
        self.deck_cards.pop(-1)
        return self.dealt_card
        
    
    def __str__(self):
        # return a string representing the deck
        
        s = "Deck Contains "
        for i in range(len(self.deck_cards)):
            s += str(self.deck_cards[i]) + " "
        return s
    


#define event handlers for buttons
def deal():
    ''' Shuffles deck, creates player/dealer hands,
    and prints out what is in each hand'''
    
    global outcome, in_play, dealer_hand, my_hand, play_deck
    play_deck = Deck()
    play_deck.shuffle()
    my_hand = Hand()
    dealer_hand = Hand()
    #print my_hand
    #print dealer_hand
    #print play_deck
    my_hand.add_card(play_deck.deal_card())
    my_hand.add_card(play_deck.deal_card())
    dealer_hand.add_card(play_deck.deal_card())
    dealer_hand.add_card(play_deck.deal_card())
    print ("Your " + str(my_hand))
    print ("Value of your cards is " + str(my_hand.get_value()))
    print " "
    print ("Dealer " + str(dealer_hand))
    print ("Value of dealer's cards is " + str(dealer_hand.get_value()))
    print " "
    print "Hit or Stand?"
    in_play = True

def hit():
    global in_play, my_hand, play_deck, outcome, score
    if in_play == True:
        if my_hand.get_value() <= 21:
            my_hand.add_card(play_deck.deal_card())
            print ("You hit!")
            print ("Your " + str(my_hand))
            print ("Value of your cards is " + str(my_hand.get_value()))
            if my_hand.get_value() > 21:
                print "You busted! Dealer Wins!"
                score -= 1
                print ("Game score is " + str(score))
                print " "
                in_play = False
            else:
                print "Hit or Stand?"
                print " "
            
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play, my_hand, play_deck, dealer_hand, outcome, score
    
    if in_play == True:
        print ("You stand with a " + str(my_hand.get_value()))
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(play_deck.deal_card())
            print ("Dealer hits")
            print ("Dealer " + str(dealer_hand))
        if dealer_hand.get_value() > 21:
            print ("Dealer busts!")
            print "You Win!"
            score += 1
            print ("Game score is " + str(score))
            print " "
            in_play = False
                
        elif dealer_hand.get_value() >= my_hand.get_value():
            print "You Lost! Dealer Wins!"
            score -= 1
            print ("Game score is " + str(score))
            print " "
            in_play = False
        
        else:
            print "You Win!"
            score += 1
            print ("Game score is " + str(score))
            print " "
            in_play = False
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", (400, 100), 24, 'Black')
    canvas.draw_text("Player Hand", (100, 420), 20, 'Black')
    canvas.draw_text("Score " + str(score), (400, 130) , 20, "Black")
    my_hand.draw(canvas, [160, 450])
    #dealer_hand.draw(canvas, [0, 20])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
#frame
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
