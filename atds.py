#!/usr/bin/env python3

"""
atds.py
Advanced Topics Data Structures
A collection of data types for the Advanced Topics class.
"""

__author__ = "Evan Chen"
__version__ = "2026-02-12"

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new):
        self.data = new

    def set_next(self, new):
        self.next = new

    def __repr__(self):
        return "Node[data=" + self.data + ",next=" + self.next.__repr__() + "]"

class Deque():
    def __init__(self):
        """Creates an empty deque"""
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.deque.pop(0)

    def remove_rear(self):
        if not self.is_empty():
            return self.deque.pop()
    
    def peek_front(self):
        if not self.is_empty():
            return self.deque[0]
    
    def peek_rear(self):
        if not self.is_empty():
            return self.deque[-1]
        
    def size(self):
        return len(self.deque)
    
    def is_empty(self):
        return self.size() == 0
    
    def __str__(self):
        return str(self.deque)


class Queue():
    def __init__(self):
        """Creates an empty queue"""
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return self.size() == 0
    
    def __str__(self):
        return str(self.queue)
    
class Stack():
    def __init__(self):
        """Creates an empty stack. As a list"""
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return self.size() == 0
    
    def __str__(self):
        return str(self.stack)


def main():
    """Main function of the script."""
    pass

if __name__ == "__main__":
    main()
