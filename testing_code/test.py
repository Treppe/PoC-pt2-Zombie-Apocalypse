"""
Lightweight testing class inspired by unittest from Pyunit
https://docs.python.org/2/library/unittest.html
Note that code is designed to be much simpler than unittest
and does NOT replicate unittest functionality
"""
import user47_lJ2dChjO1O_3 as zombie

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
            print
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
#obstacle_list = [(1, 2), (3, 4)]
#zombie_list = [(3, 3), (1, 1)]
#human_list = [(2, 4), (4, 3)]
#apoc = zombie.Apocalypse(5, 5, obstacle_list, zombie_list, human_list)
#print "Apoc full:"
#print apoc
#print
#apoc.clear()
#print "Apoc clear:"
#print apoc
#print
#
# def add_zombies(self, row, col) test:
#apoc = zombie.Apocalypse(5, 5)
#apoc.add_zombie(1, 3)
#print apoc

# def num_zombies(self) test:
zomb_list = [(1,1), (2,2), (3,4)]
apoc = zombie.Apocalypse(5, 5, zombie_list = zomb_list)
suite.run_test(apoc.num_zombies(), 3, "Test 3a: num_zombies()")
apoc.add_zombie(1, 1)
suite.run_test(apoc.num_zombies(), 3, "Test 3b: num_zombies()")
apoc = zombie.Apocalypse(5, 5)
suite.run_test(apoc.num_zombies(), 0, "Test 3c: num_zombies()")

# def zombies(self) test:
apoc = zombie.Apocalypse(5, 5)
suite.run_test(apoc.zombies(), None, "Test 4a: zombie()")
apoc.add_zombie(1, 1)
apoc.add_zombie(2 ,2)
apoc.add_zombie(3, 3)
suite.run_test(apoc.zombies(), [(1, 1), (2, 2), (3, 3)]), "Test 4b: zombie()"

# def zombies(self) test:
apoc = zombie.Apocalypse(5, 5)
apoc.add_human(1, 1)
apoc.add_human(2, 2)
print apoc
print
apoc.add_human(1, 1)
print apoc

suite.report_results()




