"""
Mini-max Tic-Tac-Toe 
By Kevin McDonald
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    
    choice = (-1, (-1, -1))
    #Base case is game is already over
    if board.check_win() != None:
        return SCORES[board.check_win()], (-1, -1)
    
    else:
        #look at possible moves given current board
        for move in board.get_empty_squares():
            clone_board = board.clone()
            
            clone_board.move(move[0],move[1],player)
            score = mm_move(clone_board, provided.switch_player(player))[0]
            
            #If a winning score, return that move
            if score * SCORES[player] == 1:
                return score, move
            
            elif score * SCORES[player] > choice[0]:
                choice = (score,move)
                
            elif choice[0] == -1:
                choice = (choice[0], move)
                
    return choice[0] * SCORES[player], choice[1]

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
