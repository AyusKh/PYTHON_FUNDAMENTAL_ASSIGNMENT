# utils.py
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input(prompt):
    """Get user input with a given prompt and return it."""
    return input(prompt)
