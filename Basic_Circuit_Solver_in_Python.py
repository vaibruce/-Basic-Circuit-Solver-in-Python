#Basic_Circuit_Solver_in_Python
#Write your code here


class TestKVL(unittest.TestCase):

    # Testing KVL function
    def test_solve_kvl(self):
        self.assertTrue(solve_kvl([10, -5, -5]))  # Should satisfy KVL
        self.assertFalse(solve_kvl([10, -5, -3]))  # Should violate KVL

# Running the KVL tests
unittest.main(argv=[''], verbosity=2, exit=False)
