# -Basic-Circuit-Solver-in-Python
A Python program to solve simple DC circuits using Ohm’s law and Kirchhoff’s laws.

class TestKVL(unittest.TestCase):

    # Testing KVL function
    def test_solve_kvl(self):
        self.assertTrue(solve_kvl([10, -5, -5]))  # Should satisfy KVL
        self.assertFalse(solve_kvl([10, -5, -3]))  # Should violate KVL

# Running the KVL tests
unittest.main(argv=[''], verbosity=2, exit=False)
