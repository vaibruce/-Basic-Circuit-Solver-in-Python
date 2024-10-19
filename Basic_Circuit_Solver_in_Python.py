#Basic_Circuit_Solver_in_Python
#Write your code here

def calculate_current(voltage, resistance):
    """Calculates the current using Ohm's Law: I = V / R"""
    if resistance == 0:
        raise ValueError("Resistance cannot be zero.")
    return voltage / resistance

def calculate_voltage(current, resistance):
    """Calculates the voltage using Ohm's Law: V = I * R"""
    return current * resistance

# Example usage of Ohm's Law
# voltage = 10, resistance = 5
print(f"Current: {calculate_current(10, 5)} A")  # Output: 2 A
print(f"Voltage: {calculate_voltage(2, 5)} V")   # Output: 10 V


def solve_kcl(node_currents):
    """Validates Kirchhoff's Current Law (KCL): Sum of currents at a node should be zero."""
    total_current = sum(node_currents)
    if total_current == 0:
        return True  # KCL is satisfied
    else:
        return False  # KCL is violated
        # Example usage of KCL
node_currents = [3, -2, -1]  # Entering and leaving currents at a node
print(f"KCL Valid: {solve_kcl(node_currents)}")  # Output: True

def solve_kvl(loop_voltages):
    """Validates Kirchhoff's Voltage Law (KVL): Sum of voltages in a loop should be zero."""
    total_voltage = sum(loop_voltages)
    if total_voltage == 0:
        return True  # KVL is satisfied
    else:
        return False  # KVL is violated

# Example usage of KVL
loop_voltages = [10, -5, -5]  # Voltages in a closed loop
print(f"KVL Valid: {solve_kvl(loop_voltages)}")  # Output: True


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

class TestKVL(unittest.TestCase):

    # Testing KVL function
    def test_solve_kvl(self):
        self.assertTrue(solve_kvl([10, -5, -5]))  # Should satisfy KVL
        self.assertFalse(solve_kvl([10, -5, -3]))  # Should violate KVL

# Running the KVL tests
unittest.main(argv=[''], verbosity=2, exit=False)
