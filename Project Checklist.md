# Project Checklist

[Phase 1 - Apocalypse class](#Phase 1 - Apocalypse Class)
		[Phase 2 - Breadth-First Search](#Phase 2 - Breadth-First Search)

[Phase 3 - Update Positions](#Phase 3 - Update Positions)

## Phase 1 - Apocalypse Class

In phase one, we will implement the basic methods for the Apocalypse class. We suggest that you start from [this template](http://www.codeskulptor.org/#poc_zombie_template.py). Note that the Apocalypse class is a subclass of the [Grid class](http://www.codeskulptor.org/#poc_grid.py) and inherits all of its methods.

The template contains an implementation of the _ _init_ _ method for the Apocalypse class. The initializer takes two required arguments grid_height and grid_width. The initializer also takes three optional arguments obstacle_list, zombie_list, and human_list which are lists of cells that initially contain obstacles, zombies and humans, respectively. For phase one, your task is to implement the remaining seven Apocalypse methods:

### 1. def clear(self):

Reset all cells in the grid to be passable and reinitialize the human and zombie lists to be empty. Remember that you can use the clear method from the poc_grid. Grid class to clear the grid of impassable cells. Examine the implementation of the _ _init_ _ method for how to call this method.

- [x]  1.1. Implement test for method
- [x]  1.2. Implement method
- [x] 1.3. Test method
- [x] 1.4. Fix bugs
- [x] 1.5. Commit changes

### 2. def add_zombie(self,  row, col)

Add a zombie to the zombie list at the supplied row and column.

- [x]  2.1. Implement test for method
- [x]  2.2. Implement method
- [x] 2.3. Test method
- [x] 2.4. Fix bugs
- [x] 2.5. Commit changes

### 3. def num_zombie(self)

Return the number of zombies in the zombie list.

- [x]  3.1. Implement test for method
- [x]  3.2. Implement method
- [x] 3.3. Test method
- [x] 3.4. Fix bugs
- [x] 3.5. Commit changes

### 4. def zombies(self)

Generator that allows you to iterate over zombies in the zombie list. Here, a zombie is a tuple of the form (row,col) indicating the zombie's location in the grid. The generator **must** yield the zombies in the order they were added (even if they have moved). Remember that you can use a generator to implement this method in one or two lines of code.

- [x] 4.1. Implement test for method
- [x] 4.2. Implement method
- [x] 4.3. Test method
- [x] 4.4. Fix bugs
- [x] 4.5. Commit changes

### 5. def add_human(self,row,col)

 Add a human to the human list at the supplied row and column.

- [x] 5.1. Implement test for method
- [x] 5.2. Implement method
- [x] 5.3. Test method
- [x] 5.4. Fix bugs
- [x] 5.5. Commit changes

### 6. def num_humans(self)

Return the number of humans in the human list.

- [x] 6.1. Implement test for method
- [x] 6.2. Implement method
- [x] 6.3. Test method
- [x] 6.4. Fix bugs
- [x] 6.5. Commit changes

### 7. def humans(self)

 Generator that allows you to iterate over humans in the human list. The generator **must** yield the humans in the order they were added (even if they have moved). Again, you can use a generator to implement this method in one or two lines of code.

- [x] 7.1. Implement test for method
- [x] 7.2. Implement method
- [x] 7.3. Test method
- [x] 7.4. Fix bugs
- [x] 7.5. Commit changes

### 8. Phase 1 - Final

- [x] 8.1. Test all functions
- [x] 8.2. Test class in OwlTest
- [x] 8.3. Fix bugs
- [x] 8.4. Commit and push Phase 1

## Phase 2 - Breadth-First Search

 Compute a simple approximation of the distance from each cell in the grid to the nearest zombie (or human). This distance will correspond to the length of the *shortest* sequence of adjacent grid cells (a path) from the cell to a zombie. This 2D array of integer distances is a *distance field*.

### def compute_distance_field(self, entity_type)

This method returns a 2D distance field computed using the four-way distance to entities of the given type (either ZOMBIE or HUMAN). Note that entries of the computed distance fields should be zero at the entities in the specified list. Non-zero distances should be computed using the shortest path computation based on breadth-first search . These shortest paths should avoid impassable cells.

#### Breadth-First Search – High-Level description

```python
while boundary is not empty:
    current_cell  ←  dequeue boundary
    for all neighbor_cell of current_cell:
        if neighbor_cell is not in visited:
            add neighbor_cell to visited
            enqueue neighbor_cell onto boundary
```

### Breadth-First Search Implementing Steps

- [x] Create a new grid visited of the same size as the original grid and initialize its cells to be empty.
- [x] Create a 2D list distance_field of the same size as the original grid and initialize each of its entries to be the product of the height times the width of the grid. (This value is larger than any possible distance.)
- [x] Create a queue boundary that is a **copy** of either the zombie list or the human list. For cells in the queue, initialize visited to be FULL and distance_field to be zero. We recommend that you use our [Queue class](http://www.codeskulptor.org/#poc_queue.py).
- [x] Finally, implement a modified version of the BFS search described above. For each neighbor_cell in the inner loop, check whether the cell has not been visited and is passable. If so, update the visited grid and the boundary queue as specified. In this case, also update the neighbor's distance to be the distance to current_cell plus one ($\color{red}{\verb|distance_field[current_cell[0]][current_cell[1]] + 1|}$)

## Phase 3 - Update Positions

In phase three, your task is to implement two final methods that update the positions of the zombies and humans, respectively

### def  move_humans(self,zombie_distance_field)

This method updates the entries in the human list to model humans avoiding zombies. Each human either stays in its current cell or moves to a neighboring cell to maximize its distance from the zombies. Specifically, humans move to a cell that maximize their distance from the zombies according to the supplied $ \color{red}{\verb|zombie_distance_field|}$. In the case where several cells shared the same maximal distance, we recommend (but do not require) choosing among these cells at random.

- [x] Implement test for method
- [x] Implement method
- [x] Test method
- [x] Fix bugs
- [x] Commit changes

### def move_zombies(self,human_distance_field)

This method updates the entries in the zombie list to model zombies chasing humans. Each zombie either stays in its current cell or moves to a neighboring cell to minimize its distance to the humans. Specifically, zombies moves to the cell that minimizes their distance to the humans according to the supplied $\color{red}{\verb|human_distance_field|}$. In the case where several cells shared the same minimal distance, we recommend choosing (but do not require) among these cells at random.

- [x] Implement test for method
- [x] Implement method
- [x] Test method
- [x] Fix bugs
- [x] Commit changes

[#Phase 3 - Update Positions]: 

[#Phase 3 - Update Positions]: 
[#Phase-3 —Update-Positions]: 