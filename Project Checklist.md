# Project Checklist

[TOC]



[Phase 1 - Apocalypse class](#Phase-1—Apocalypse-Class)

[Phase 2](#Phase-2)

## Phase 1 - Apocalypse Class

In phase one, we will implement the basic methods for the Apocalypse class. We suggest that you start from [this template](http://www.codeskulptor.org/#poc_zombie_template.py). Note that the Apocalypse class is a subclass of the [Grid class](http://www.codeskulptor.org/#poc_grid.py) and inherits all of its methods.

The template contains an implementation of the _ _init_ _ method for the Apocalypse class. The initializer takes two required arguments grid_height and grid_width. The initializer also takes three optional arguments obstacle_list, zombie_list, and human_list which are lists of cells that initially contain obstacles, zombies and humans, respectively. For phase one, your task is to implement the remaining seven Apocalypse methods:

### 1. def clear(self):

Reset all cells in the grid to be passable and reinitialize the human and zombie lists to be empty. Remember that you can use the clear method from the poc_grid.Grid class to clear the grid of impassable cells. Examine the implementation of the _ _init_ _ method for how to call this method.

- [ ]  1.1. Implement test for method
- [ ]  1.2. Implement method
- [ ] 1.3. Test method
- [ ] 1.4. Fix bugs
- [ ] 1.5. Commit changes

### 2. def add_zombies(self,  row, col)

Add a zombie to the zombie list at the supplied row and column.

- [ ]  2.1. Implement test for method
- [ ]  2.2. Implement method
- [ ] 2.3. Test method
- [ ] 2.4. Fix bugs
- [ ] 2.5. Commit changes

### 3. def num_zombie(self, row, col)

Return the number of zombies in the zombie list.

- [ ]  3.1. Implement test for method
- [ ]  3.2. Implement method
- [ ] 3.3. Test method
- [ ] 3.4. Fix bugs
- [ ] 3.5. Commit changes

### 4. def zombies(self)

Generator that allows you to iterate over zombies in the zombie list. Here, a zombie is a tuple of the form (row,col) indicating the zombie's location in the grid. The generator **must** yield the zombies in the order they were added (even if they have moved). Remember that you can use a generator to implement this method in one or two lines of code.

- [ ] 4.1. Implement test for method
- [ ] 4.2. Implement method
- [ ] 4.3. Test method
- [ ] 4.4. Fix bugs
- [ ] 4.5. Commit changes

### 5. def add_human(self,row,col)

 Add a human to the human list at the supplied row and column.

- [ ] 5.1. Implement test for method
- [ ] 5.2. Implement method
- [ ] 5.3. Test method
- [ ] 5.4. Fix bugs
- [ ] 5.5. Commit changes

### 6. defnum_humans(self)

Return the number of humans in the human list.

- [ ] 6.1. Implement test for method
- [ ] 6.2. Implement method
- [ ] 6.3. Test method
- [ ] 6.4. Fix bugs
- [ ] 6.5. Commit changes

### 7. defhumans(self)

 Generator that allows you to iterate over humans in the human list. The generator **must** yield the humans in the order they were added (even if they have moved). Again, you can use a generator to implement this method in one or two lines of code.

- [ ] 7.1. Implement test for method
- [ ] 7.2. Implement method
- [ ] 7.3. Test method
- [ ] 7.4. Fix bugs
- [ ] 7.5. Commit changes

### 8. Phase 1 - Final

- [ ] 8.1. Test all functions
- [ ] 8.2. Test class in OwlTest
- [ ] 8.3. Fix bugs
- [ ] 8.4. Commit and push Phase 1

## Phase 2