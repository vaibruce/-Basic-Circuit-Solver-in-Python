import unittest

class TestCircuitSolver(unittest.TestCase):

    # Testing Ohm's Law functions
    def test_calculate_current(self):
        self.assertEqual(calculate_current(10, 5), 2)
        self.assertRaises(ValueError, calculate_current, 10, 0)

    def test_calculate_voltage(self):
        self.assertEqual(calculate_voltage(2, 5), 10)

    # Testing KCL
    def test_solve_kcl(self):
        self.assertTrue(solve_kcl([3, -2, -1]))  # Should satisfy KCL
        self.assertFalse(solve_kcl([3, -2, -2]))  # Should violate KCL

# Running the tests
unittest.main(argv=[''], verbosity=2, exit=False)
              