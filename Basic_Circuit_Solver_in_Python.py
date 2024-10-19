#Basic_Circuit_Solver_in_Python
#Write your code here
def solve_kcl(node_currents):
    """Validates Kirchhoff's Current Law (KCL): Sum of currents at a node should be zero."""
    total_current = sum(node_currents)
    if total_current == 0:
        return True  # KCL is satisfied
    else:
        return False  # KCL is violated
