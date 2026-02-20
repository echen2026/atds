#!/usr/bin/env python3

"""
paren_checker.py
Write a program called paren_checker.py that imports the atds module, and has a single boolean function is_valid(expr) that identifies whether a string of parentheses is legal or not. It will do this by creating a Stack object from the atds module and using it to track parentheses in the expression.
"""

__author__ = "Evan Chen"
__version__ = "2026-02-12"

import atds

def is_valid(expr):
    stack = atds.Stack()
    for char in expr:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


def main():
    """Main function of the script."""
    pass

if __name__ == "__main__":
    main()