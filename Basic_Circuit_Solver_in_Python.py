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

