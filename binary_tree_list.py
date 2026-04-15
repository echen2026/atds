#!/usr/bin/env python3

"""
binary_tree.py
Module Docstring
"""

__author__ = "Evan Chen"
__version__ = "2026-04-09"

def binary_tree(val):
    return [val, [], []]

def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

def insert_left(root, new_branch):
    temp = root[1]
    root[1] = [new_branch, temp, []]

def insert_right(root, new_branch):
    temp = root[2]
    root[2] = [new_branch, [], temp]


def main():
    t = binary_tree(3)
    print("Instruction: t = binary_tree(3)")
    print("Result:", t)
    print("Expect: [3, [], []]")
    insert_left(t, 4)
    print("Instruction: insert_left(t, 4)")
    print("Result:", t)
    print("Expect: [3, [4, [], []], []]")
    insert_left(t, 5)
    print("Instruction: insert_left(t, 5)")
    print("Result:", t)
    print("Expect: [3, [5, [4, [], []], []], []]")
    insert_right(t, 6)
    print("Instruction: insert_right(t, 6)")
    print("Result:", t)
    print("Expect: [3, [5, [4, [], []], []], [6, [], []]]")
    insert_right(t, 7)
    print("Instruction: insert_right(t, 7)")
    print("Result:", t) 
    print("Expect: [3, [5, [4, [], []], []], [7, [], [6, [], []]]]")
    l = get_left_child(t)
    print("Instruction: l = get_left_child(t)")
    print("Result: l =", l)
    print("Expect: l = [5, [4, [], []], []]")
    set_root_val(l, 9)
    print("Instruction: set_root_val(l, 9)")
    print("Result: l =", l)
    print("Expect: l = [9, [4, [], []], []]")
    insert_left(l, 11)
    print("Instruction: insert_left(l, 11)")
    print("Result:", t)
    print("Expect: [3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]")
    print("Instruction: print(get_right_child(get_right_child(t)))")
    print("Result:", get_right_child(get_right_child(t)))
    print("Expect: [6, [], []]")   

if __name__ == "__main__":
    main()