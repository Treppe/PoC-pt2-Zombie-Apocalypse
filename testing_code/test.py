"""
Lightweight testing class inspired by unittest from Pyunit
https://docs.python.org/2/library/unittest.html
Note that code is designed to be much simpler than unittest
and does NOT replicate unittest functionality
"""
import user47_lJ2dChjO1O_10 as zombie

class TestSuite:
    """
    Create a suite of tests similar to unittest
    """
    def __init__(self):
        """
        Creates a test suite object
        """
        self.total_tests = 0
        self.failures = 0
    
    
    def run_test(self, computed, expected, message = ""):
        """
        Compare computed and expected
        If not equal, print message, computed, expected
        """
        self.total_tests += 1
        if computed != expected:
            msg = message + " Computed: " + str(computed)
            msg += " Expected: " + str(expected)
            print msg
            self.failures += 1
    
    def report_results(self):
        """
        Report back summary of successes and failures
        from run_test()
        """
        msg = "Ran " + str(self.total_tests) + " tests. "
        msg += str(self.failures) + " failures."
        print
        print msg
               
suite = TestSuite()

# def clear(self) test:
obstacle_list = [(1, 2), (3, 4)]
zombie_list = [(3, 3), (1, 1)]
human_list = [(2, 4), (4, 3)]
apoc = zombie.Apocalypse(5, 5, obstacle_list, zombie_list, human_list)
suite.run_test(apoc.get_humans(), human_list, "Test #1: get_humans()")
suite.run_test(apoc.get_zombies(), zombie_list, "Test #2: get_zombies()")
print apoc # Check obstacles
apoc.clear()
suite.run_test(apoc.get_humans(), [], "Test #3a: clear()")
suite.run_test(apoc.get_zombies(), [], "Test #3b: clear()")
print apoc # Check obstacles

# def add_zombies(self, row, col) test:
apoc = zombie.Apocalypse(5, 5)
apoc.add_zombie(1, 3)
apoc.add_zombie(2, 2)
suite.run_test(apoc.get_zombies(), [(1, 3), (2, 2)], "Test #4a: add_zombie()")
apoc.add_zombie(2, 2)
suite.run_test(apoc.get_zombies(), [(1, 3), (2, 2)], "Test #4b: add_zombie()")

# def num_zombies(self) test:
zomb_list = [(1,1), (2,2), (3,4)]
apoc = zombie.Apocalypse(5, 5, zombie_list = zomb_list)
suite.run_test(apoc.num_zombies(), 3, "Test 5a: num_zombies()")
apoc.add_zombie(1, 1)
suite.run_test(apoc.num_zombies(), 3, "Test 5b: num_zombies()")
apoc = zombie.Apocalypse(5, 5)
suite.run_test(apoc.num_zombies(), 0, "Test 5c: num_zombies()")

# def zombies(self) test:
apoc = zombie.Apocalypse(5, 5)
suite.run_test(list(apoc.zombies()), [], "Test 6a: zombies()")
apoc.add_zombie(1, 1)
apoc.add_zombie(2 ,2)
apoc.add_zombie(3, 3)
suite.run_test(list(apoc.zombies()), [(1, 1), (2, 2), (3, 3)], "Test 6b: zombie()")

# def add_human(self, row, col) test:
apoc = zombie.Apocalypse(5, 5)
apoc.add_human(1, 1)
apoc.add_human(2, 2)
suite.run_test(apoc.get_humans(), [(1, 1), (2, 2)], "Test #7a: add_human()")
apoc.add_human(1, 1)
suite.run_test(apoc.get_humans(), [(1, 1), (2, 2)], "Test #7b: add_human()")

# def num_humans(self) test:
apoc = zombie.Apocalypse(5, 5)
suite.run_test(apoc.num_humans(), 0, "Test #8a: num_humans()")
apoc.add_human(1, 1)
suite.run_test(apoc.num_humans(), 1, "Test #8b: num_humans()")

suite.report_results()




