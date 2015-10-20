"""
Monte Carlo Tic-Tac-Toe Player
Game by Kevin M
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants
EMPTY = 1
PLAYERX = 2
PLAYERO = 3 
DRAW = 4

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 50         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

#Initial variables required for below functions

game_board = provided.TTTBoard(3)
#score_board = [[0 for col in range(3)] 
                      #for row in range(3)]
#print score_board
#print game_board.get_empty_squares()
#print random.choice(game_board.get_empty_squares())
#print " "
#print game_board.__str__()
#print board.get_dim()



# Add your functions here.


def mc_trial(board,player):
    ''' 
    Function to randomly place tiles for machine player on game
    board to play out a complete game of TTT
    '''
    
    for dummy_items in range(len(board.get_empty_squares())):
        while board.check_win() == None:            
            pick_space = random.choice(board.get_empty_squares())
            board.move(pick_space[0],pick_space[1],player)
            player = provided.switch_player(player)            
    #print board.__str__()
    print board.check_win()

def mc_update_scores(scores,board,player):
    '''Takes a completed game board from mc_trial and scores the game,
    updating score_board with the running total for the desired
    number of trials
    '''
    
    #Takes game board and score board, looks at each square in game board 
    
    #then scores it appropriately based on who won the game
    
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            player = board.square(row,col)
            if player == PLAYERX:
                if board.check_win() == PLAYERX:
                    scores[row][col] += SCORE_CURRENT
                elif board.check_win() == PLAYERO:
                    scores[row][col] += -SCORE_OTHER
            elif player == PLAYERO:
                if board.check_win() == PLAYERO:
                    scores[row][col] += SCORE_CURRENT
                elif board.check_win() == PLAYERX:
                    scores[row][col] += -SCORE_OTHER
                    
            
    

def get_best_move(board, scores):
    emptys_on_board = board.get_empty_squares()
    score_emptys = []
    max_list = []
    
    #Pulls scores for empty squares on game board and creates list 
    
    #of scores
    
    for empty in emptys_on_board:
        row = empty[0]
        col = empty[1]
        score_emptys.append(scores[row][col])
        
    print emptys_on_board
    print score_emptys
            
    #Find max value in score_emptys
    
    max_value = max(score_emptys)
    
    #Pull coordinate for square(s) with max value

    for empty in emptys_on_board:
        row = empty[0]
        col = empty[1]
        if scores[row][col] == max_value:
            max_list.append(empty)
            
    return random.choice(max_list)

def mc_move(board, player, trials):
    '''
    Runs the simulation to find a move for the machine player
    by utilizing the above 3 functions to calculate an optimal play
    '''
    
    #Create initial scoreboard for use in functions, all 0s to start
    score_board = [[0 for dummy_col in range(board.get_dim())] 
                    for dummy_row in range(board.get_dim())]
    
    #Main function to run other created functions and return best move
    for dummy_trial in range(trials):
        cloned = board.clone()
        print cloned
        mc_trial(cloned, player)
        print cloned
        mc_update_scores(score_board, cloned, player)
        
    return get_best_move(board, score_board)


#mc_trial(provided.TTTBoard(4),provided.PLAYERX)
#mc_update_scores(
# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
