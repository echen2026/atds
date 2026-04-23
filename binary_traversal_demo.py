#!/usr/bin/env python3

"""
binary_traversal_demo.py
Module Docstring
"""

__author__ = "Evan Chen"
__version__ = "2026-04-20"

from binary_tree_class import BinaryTree

def preorder(bt):
    if bt == None:
        return []
    else:
        return [bt.get_root_val()] + preorder(bt.get_left_child()) + preorder(bt.get_right_child())

def postorder(bt):
    if bt == None:
        return []
    else:
        return postorder(bt.get_left_child()) + postorder(bt.get_right_child()) + [bt.get_root_val()]

def inorder(bt):
    if bt == None:
        return []
    else:
        return inorder(bt.get_left_child()) + [bt.get_root_val()] + inorder(bt.get_right_child())

def main():
    """Main function of the script."""
    bt = BinaryTree(None)
    bt.set_root_val("a")
    bt.insert_left("h")
    bt.insert_left("d")
    bt.insert_left("b")
    bt.get_left_child().get_left_child().insert_right("i")
    bt.get_left_child().insert_right("j")
    bt.get_left_child().insert_right("e")
    bt.insert_right("g")
    bt.get_right_child().insert_right("c")
    bt.get_right_child().insert_left("f")
    bt.get_right_child().get_right_child().insert_left("k")
    
                         

    print("Preorder:", preorder(bt))
    print("Postorder:", postorder(bt))
    print("Inorder:", inorder(bt))

if __name__ == "__main__":
    main()