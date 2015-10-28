"""
Student code for Word Wrangler game
by Kevin McDonald
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    #Create new list that will be deduped
    deduped_list = []
    
    for item in list1:
        if item not in deduped_list:
            deduped_list.append(item)
        
    return deduped_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """        
    intersect_list = []
    
    #takes each element from list1, compares it to everything in list 2
    
    #appends to intersect_list if there is a match
    
    for item in list1:
        for dummy_idx in range(len(list2)):
            if item == list2[dummy_idx]:
                intersect_list.append(item)
                break
                    
    return intersect_list



# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """ 
    merged_list = []
    
    idx1 = 0
    idx2 = 0
    
    while idx1 <= (len(list1) - 1) or idx2 <= (len(list2)):
        
        if idx1 == (len(list1)) or idx2 == (len(list2)):
            break
            
        
        if list1[idx1] < list2[idx2]:
            merged_list.append(list1[idx1])
            idx1 += 1
            
        elif list1[idx1] > list2[idx2]:
            merged_list.append(list2[idx2])
            idx2 += 1
            
        elif list1[idx1] == list2[idx2]:
            merged_list.append(list1[idx1])
            idx1 += 1
        
        
        
    if idx1 == len(list1):
        while idx2 <= (len(list2) - 1):
            merged_list.append(list2[idx2])
            idx2 += 1
                
    if idx2 == len(list2):
        while idx1 <= (len(list1) - 1):
            merged_list.append(list1[idx1])
            idx1 += 1                
                              
    return merged_list
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    lower_list = []
    upper_list = []
    
    if len(list1) <= 1:
        return list1
    
    elif len(list1) > 1:
        mid = (len(list1) / 2)
               
        lower_list = merge_sort(list1[:mid])                
        upper_list = merge_sort(list1[mid:])
                            
    return merge(lower_list,upper_list)
    

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    new_list = []
    
    if len(word) < 1:
        return [word]
    
    else:
        first = word[0]
        rest = word[1:]
        print "first :",first, "rest :", rest
        
        rest_strings = gen_all_strings(rest)
        
 
        for strings in rest_strings:
            for idx in range((len(strings) + 1)):
                new_list.append(strings[:idx] + first + strings[idx:])
    
    
    return new_list + rest_strings


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

    
    
