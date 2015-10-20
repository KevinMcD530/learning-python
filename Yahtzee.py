"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)


import random

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    #print answer_set
    return answer_set


def gen_sorted_sequences(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences
    """    
    all_sequences = gen_all_sequences(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)

#print gen_sorted_sequences
def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.
    
    hand: full yahtzee hand
    
    Returns an integer score 
    """
    #score list keeps a record of the possible summed totals
    
    #max_score will find the max out of score list and be returned
    score_list = []
    max_score = 0
    
    for dummy_num in hand:
        x = hand.count(dummy_num)
        score_for_num = x * dummy_num
        score_list.append(score_for_num)
    
    #print score_list
    score_list.sort()
    #print "Max score is"
    max_score = score_list[-1]
    #print score_list[-1]
    
    return max_score


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    #Create set of possible dice rolls for free dice
    append_outcomes = [1,2,3,4,5,6]
    append_set = gen_all_sequences(append_outcomes,num_free_dice)    
    #print "APPEND SET",append_set
    #print "Length of append_set:",len(append_set)
    
    #score append_set + held dice and sum them
    total_score = 0
    
    for dummy_items in append_set:
        #convert append_set iterable and and hand into list
        
        #combine the above to create a hand to score
        list_items = list(dummy_items)
        hand_dice = list(held_dice)
        score_hand = list_items + hand_dice
        #print "Score hand is:",score_hand
        
        #sum all scores across all hands
        total_score += score(score_hand)
        #print "TOTAL SCORE ON THIS ITERATION IS",total_score
    #print "total score after all iterations is", total_score
    
    exp_value = float(float(total_score)  / float(len(append_set)))
    #print "Expected value is:", float(exp_value)
                                    
    
    
    return float(exp_value)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    # Hold_set will be the set of all possible combos of dice holds
    #sorted_hand = hand.sort()

    hold_set = set([()])
    
    for item in hand:
        temp = hold_set.copy()
        #print "temp type", type(temp)
        for dummy_items in hold_set:
            
            #Create variables for new 
            new_sequence = list(dummy_items)
            new_sequence.append(item)
            #print "NEW SEQUENCE",new_sequence
            
            #sort the new_sequence to ensure duplicates dont'
            
            #make it over
            
            new_sequence = sorted(new_sequence)
            
            #turn new_Sequence into tuples
            new_sequence = tuple(new_sequence)
            
            #append temp with tuple we've created]
            if new_sequence not in temp:
                temp.add(new_sequence)    
            
            #hold_set = hold_set + [tuple(subset) + (item, )]
        
        #print "temp type", type(temp)        
        hold_set = temp
        #print "HOLD SET HOLDETH",hold_set
        
    #hold_set = sorted(hold_set)
    #hold_set
    return hold_set



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    #holds set will have all possible holds given hand
    holds_set = gen_all_holds(hand)
    max = 0
    best_hand = ()
    print holds_set
    
    for dummy_item in holds_set:
        test_hand = dummy_item
        #print "testing hand to be max: ",test_hand
        hand_value = expected_value(test_hand,num_die_sides,len(hand)-len(test_hand))
        if max < hand_value:
            max = hand_value
            best_hand = dummy_item
            
    #print "Best hand is:",best_hand
    return (max, best_hand)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
#print gen_all_sequences(set([1,2,3,4,5,6]),1)
#print gen_all_holds([1,2,3])
                        
#test_hand = ((1,1,2,3,4))
#print test_hand.count(1)
run_example()

#strategy([1,2,3],6)

#expected_value(([2,2]),6,2)
#print gen_all_sequences(6,5)
#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    


