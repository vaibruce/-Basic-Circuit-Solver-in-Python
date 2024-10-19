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
