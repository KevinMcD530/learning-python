"""
Student portion of Zombie Apocalypse mini-project
by: Kevin McDonald
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row,col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list) 
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        #initialize core grids and boundary queue
        
        #visited = [[EMPTY for dummy_col in range(self._grid_width)]
                       #for dummy_row in range(self._grid_height)]
            
        visited = poc_grid.Grid(self._grid_height,self._grid_width)
        
        visited.clear()
        
        max_distance = self._grid_height * self._grid_width
        distance_field = [[max_distance for dummy_col in range(self._grid_width)]
                       for dummy_row in range(self._grid_height)]
        
        print "distance_field is :", distance_field
        
        
        
        #check if we need to copy human or zombie list and populate queue
        entity_list = []
        if entity_type == HUMAN:
            entity_list = self._human_list
        else:
            entity_list = self._zombie_list
            
        #Create boundary Queue
        
        boundary = poc_queue.Queue()
        print "boundary type is :", type(boundary)       
                
        #Initialize boundary locations to full in visited and distance to be 0
        
        for entity in entity_list:
            row = entity[0]
            col = entity[1]
            poc_queue.Queue.enqueue(boundary, entity)
            poc_grid.Grid.set_full(visited, row, col)
            distance_field[row][col] = 0
        
        print "updated visited is :", visited.__str__()
        print "updated distance fields is :", distance_field                                     
        
        #BFS of items in boundary
        
        while len(boundary) > 0:
            cell = poc_queue.Queue.dequeue(boundary)
            neighbors = poc_grid.Grid.four_neighbors(self,cell[0],cell[1])
            for neighbor in neighbors:
                row = neighbor[0]
                col = neighbor[1]
                if poc_grid.Grid.is_empty(visited, row, col) == True and poc_grid.Grid.is_empty(self,row,col) == True:
                    
                    poc_grid.Grid.set_full(visited, row, col)
                    poc_queue.Queue.enqueue(boundary, neighbor)
                    
                    distance_field[row][col] = distance_field[cell[0]][cell[1]] + 1
                    
        
        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        #temp_list = self._human_list.copy()
        new_human_list = []
        
        
        for human in self._human_list:
            max_distance = float('-inf')
            row = human[0]
            col = human[1]
            neighbors = poc_grid.Grid.eight_neighbors(self,row,col) + [(row,col)]
            
            best_move = []
            
            for neighbor in neighbors:
                if poc_grid.Grid.is_empty(self, neighbor[0], neighbor[1]):
                    distance = zombie_distance_field[neighbor[0]][neighbor[1]]
                    if distance > max_distance:
                        max_distance = distance
                        best_move = [neighbor]
                    elif distance == max_distance:
                        best_move.append(neighbor)
            new_human_list.append(random.choice(best_move))
        self._human_list = new_human_list

    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        new_zombie_list = []
        #zombies = self.zombies()
        
        for zombie in self._zombie_list:
            min_distance = float('inf')
            row = zombie[0]
            col = zombie[1]
            neighbors = poc_grid.Grid.four_neighbors(self,row,col) + [(row,col)]
            
            best_move = []
            
            for neighbor in neighbors:
                if poc_grid.Grid.is_empty(self, neighbor[0], neighbor[1]):
                    distance = human_distance_field[neighbor[0]][neighbor[1]]
                    if distance < min_distance:
                        min_distance = distance
                        best_move = [neighbor]
                    elif distance == min_distance:
                        best_move.append(neighbor)
            new_zombie_list.append(random.choice(best_move))
        self._zombie_list = new_zombie_list



# Start up gui for simulation - You will need to write some code above
# before this will work without errors


#poc_zombie_gui.run_gui(Apocalypse(30, 40))
