"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}



def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """    
    #result line is for the first compact and addition
    
    #final_line exists for the final compact following the above
    
    #Make these the same length as game_line, except populated wth zero's.
    
    result_line = [0] * len(line)
    final_line = [0] * len(line)
    
    
    #result_pos moves the index in the result line
    result_pos = 0
    
    
    #first operation to slide numbers to the left
    for num in line:
        if num != 0:
            result_line[result_pos] = num
            result_pos += 1
    #print str("Compacted list is " + str(result_line))
    #print type(result_line)
    result_pos = 0
    
    #second operation to add paired tiles
    
    for index_num in (range(len(result_line)-1)):
        if result_line[index_num] == result_line[index_num + 1]:
            result_line[index_num] = result_line[index_num] + result_line[index_num + 1]
            result_line[index_num + 1] = 0
    #print str("Merged line is " + str(result_line))
    #print type(result_line)
            
    #final operation to slide numbers to the left 2nd and final time

    for num in result_line:
        if num != 0:
            final_line[result_pos] = num
            result_pos += 1
    #print str("Final list is " + str(final_line))
    print final_line
    result_pos = 0
    return final_line
    

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # stores grid height and width and creates game board
        self.height = grid_height
        self.width = grid_width
        self.cells = []
        print "Game initialized grid is"
        self.reset()
        
        #self.__str__()
        
        # Dictionary of initial tiles corresponding to a merge
        
        #of each direction
        self.initial_cells = { UP : [[0, element] for element in range(self.get_grid_width())],
                              DOWN : [[self.get_grid_height() - 1, item] for item in range(self.get_grid_width())],
                              LEFT : [[element, 0] for element in range(self.get_grid_height())],
                              RIGHT : [[item, self.get_grid_width() - 1] for item in range(self.get_grid_height())]}
        
        print " "
        print "Initial Cells Dictionary"
        print self.initial_cells
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        print "I am resetting"
        #self.cells = [[row * 0 for row in range(self.height)] 
                      #for col in range(self.width)]
        
        self.cells = [[col * 0 for col in range(self.width)] 
                      for row in range(self.height)]
        
        self.new_tile()
        self.new_tile()
        

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        #for row in range(self.height):            
            #print self.cells[row]
        return str(self.cells)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.height
        

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width
        

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        
        #Calculate number of steps needed to traverse row based on direction
        
        if (direction == UP) or (direction == DOWN):
            steps = range(self.height)
        else:
            steps = range(self.width)
            
        
        #Create flag to identify if a move has occurred
        
        did_move = False

        #step (using direction based calc above
       
        # through each row or column
        
        for initial_tile in self.initial_cells[direction]:
            merging = []
            for step in steps:
                row = initial_tile[0] + step * OFFSETS[direction][0]
                col = initial_tile[1] + step * OFFSETS[direction][1]
                merging.append(self.cells[row][col])
            merged = merge(merging)
            for step in steps:
                row = initial_tile[0] + step * OFFSETS[direction][0]
                col = initial_tile[1] + step * OFFSETS[direction][1]
                self.cells[row][col] = merged[step]
            if merged != merging:
                did_move = True
                
                
        if did_move == True:
            self.new_tile()
            
            
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        
        available_positions = []
        for row in range(self.height):
            for col in range(self.width):
                if self.cells[row][col] == 0:
                    available_positions.append([row,col])
        #print " Available list is"
        #print available_positions
        
        if available_positions is None:
            print "There are no avaiable locations to add a tile"
        
        else: 
            #rand_tile selects one of the available spaces with a 0 value
            
            #tile_num determines if that tile will be a 2 or 4
            
            rand_tile = random.choice(available_positions)
            tile_num = random.random()
            print "Adding tile to the following location"
            print rand_tile
            
            if tile_num > 0.9:
                tile_num = 4
            else:
                tile_num = 2
            self.set_tile(rand_tile[0],rand_tile[1],tile_num)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.cells[row][col] = value
        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.cells[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(5, 4))
