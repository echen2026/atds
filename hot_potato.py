#!/usr/bin/env python3

"""
hot_potato.py
Module Docstring
"""

__author__ = "Evan Chen"
__version__ = "2026-02-17"

import random
from atds import Queue

def hot_potato(people):
    """Start/manage the hot potato game"""
    queue = Queue()
    for person in people:
        queue.enqueue(person)

    while queue.size() > 1:
        print("Current queue:", str(queue))

        numberToOut = random.randint(1, 20)
        print("The potato will pass", numberToOut+1, "times")
        for i in range(numberToOut):
            person = queue.dequeue()
            print(person, "has the potato")
            queue.enqueue(person)
        
        out = queue.dequeue()
        print(out, "is out!")
        print("-----------------------------")

    winner = queue.dequeue()
    print(winner, "is the winner!")
    

def main():
    """Main function of the script."""
    
    print("\nHot Potato Game")
    people = ["Alice", "Bob", "Charlie", "David", "Eve"]
    hot_potato(people)

if __name__ == "__main__":
    main()