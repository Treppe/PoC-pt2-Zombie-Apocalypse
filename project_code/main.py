"""
Student portion of Zombie Apocalypse mini-project
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
    
    def __str__(self):
        return str(str(poc_grid.Grid.__str__(self)) + "\n" +
                "HUMAN LIST: " + str(self._human_list) + "\n" +
                "ZOMBIE LIST: " + str(self._zombie_list))
    
    def get_humans(self):
        """
        Returns copy of human list
        """
        return list(self._human_list)
    
    def get_zombies(self):
        """
        Returns copy of zombies list
        """
        return list(self._zombie_list)
    
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
        if (row, col) not in self._zombie_list:
            self._zombie_list.append((row, col))
                
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
        if (row, col) not in self._human_list:
            self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        # Get Apocalypse grid width and height
        grid_height = poc_grid.Grid.get_grid_height(self)
        grid_width = poc_grid.Grid.get_grid_width(self)
        
        # Create a grid of visited cells
        visited = poc_grid.Grid(grid_height, grid_width)
        visited.clear()
        
        # Create distance field and fill it with grid_height*gid_width (thi value is larger then any possible distance)
        distance_field = [[grid_height * grid_width for dummy_col in range(grid_width)] 
                       for dummy_row in range(grid_height)]
        
        # Create a queue boundary that is copy of either the zombie list or the human list.
        boundary = poc_queue.Queue()
        if entity_type == ZOMBIE:
            list_copy = list(self._zombie_list)
        else:
            list_copy = list(self._human_list)
        for entity in list_copy:
            boundary.enqueue(entity)
            visited.set_full(entity[0], entity[1])
            distance_field[entity[0]][entity[1]] = 0
            
        # Modified version of BFS search
        while len(boundary) != 0:
            current_cell = boundary.dequeue()
            if entity_type == ZOMBIE:
                neighbour_list = visited.four_neighbors(current_cell[0], current_cell[1])
            else:
                neighbour_list = visited.eight_neighbors(current_cell[0], current_cell[1])
                
            for neighbour_cell in neighbour_list:
                if not visited.is_empty(neighbour_cell[0], neighbour_cell[1]):
                    visited.set_full(neighbour_cell[0], neighbour_cell[1])
                    boundary.enqueue(neighbour_cell)
                    distance_field[neighbour_cell[0]][neighbour_cell[1]] = distance_field[current_cell[0]][current_cell[1]] + 1
            

        
                
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        pass
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        pass

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Apocalypse(30, 40))
