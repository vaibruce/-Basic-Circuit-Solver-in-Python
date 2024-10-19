# Basic-Circuit-Solver-in-Python
A Python program to solve simple DC circuits using Ohm’s law and Kirchhoff’s laws.

<<<<<<< HEAD
class TestKVL(unittest.TestCase):

    # Testing KVL function
    def test_solve_kvl(self):
        self.assertTrue(solve_kvl([10, -5, -5]))  # Should satisfy KVL
        self.assertFalse(solve_kvl([10, -5, -3]))  # Should violate KVL

# Running the KVL tests
unittest.main(argv=[''], verbosity=2, exit=False)
=======
# DC Circuit Solver

## Overview
This Python command-line tool solves simple DC circuits using **Ohm’s Law**, **Kirchhoff’s Current Law (KCL)**, and **Kirchhoff’s Voltage Law (KVL)**. The program calculates the current through each branch and voltage drops across each resistor.

## Features
- Solves circuits with multiple resistors and voltage sources.
- Modular code for different components: Ohm's Law, KCL, and KVL.
- Unit tests for validation.

## Requirements
- Python 3.x
- `numpy` for solving linear equations.

## Installation
Clone the repository and install the dependencies:

```bash
git clone https://github.com/vaibruce/Basic-Circuit-Solver-in-Python.git
cd Basic-Circuit-Solver-in-Python


>>>>>>> 1ebca41dcd8258c62775c0798856b6571ef86614
