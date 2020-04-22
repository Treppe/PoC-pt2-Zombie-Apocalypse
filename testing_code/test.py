"""
Lightweight testing class inspired by unittest from Pyunit
https://docs.python.org/2/library/unittest.html
Note that code is designed to be much simpler than unittest
and does NOT replicate unittest functionality
"""
import user47_TYjGULYEir_13 as zombie

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
print "Apoc full:"
print apoc
print
apoc.clear()
print "Apoc clear:"
print apoc
print



