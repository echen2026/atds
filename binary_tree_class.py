#!/usr/bin/env python3

"""
binary_tree_class.py
The Binary Tree Abstract Data Type has the following description of methods:

BinaryTree(key) constructs a binary tree with value key and no children
get_root_val() returns the root value of this particular sub-tree
set_root_val(val) modifies the root value of this particular sub-tree
get_left_child() returns the subtree that is the left child of the current root
get_right_child() returns the subtree that is the right child of the current root
insert_left(val) creates a new binary tree and installs it as the left child of the current node, moving the current child down one level in the tree
insert_right(val) creates a new binary tree and installs it as the right child of the current node, moving the current child down one level in the tree
In a program binary_tree_class.py write a class BinaryTree that implements the Binary Tree ADT. The class will need to include the following constructor and methods:

__init__(key)
get_root_val()
set_root_val(new_val)
get_left_child()
get_right_child()
insert_left(new_left_child)
insert_right(new_right_child)
__str__()
"""

__author__ = "Evan Chen"
__version__ = "2026-04-15"

class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    def get_root_val(self):
        return self.key

    def set_root_val(self, new_val):
        self.key = new_val

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def insert_left(self, new_left_child):
        if self.left_child == None:
            self.left_child = BinaryTree(new_left_child)
        else:
            temp = BinaryTree(new_left_child)
            temp.left_child = self.left_child
            self.left_child = temp

    def insert_right(self, new_right_child):
        if self.right_child == None:
            self.right_child = BinaryTree(new_right_child)
        else:
            temp = BinaryTree(new_right_child)
            temp.right_child = self.right_child
            self.right_child = temp

    def __str__(self):
        return "BinaryTree[key=" + str(self.key) + ",left_child=" + str(self.left_child) + ",right_child=" + str(self.right_child) + "]"


def main():
    """Main function of the script."""
    pass

if __name__ == "__main__":
    main()