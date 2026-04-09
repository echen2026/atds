#!/usr/bin/env python3

"""
workday.py
workday stack task manager
https://www.crashwhite.com/advtopicscompsci/materials/assignments/daily/4-12p-workday.md.html
"""

__author__ = "Evan Chen"
__version__ = "2026-04-06"

import random
from atds import Stack

def workday(tasks, WORKDAY_MINUTES):

    current = None
    workload = Stack()
    clock = 0
    while clock < WORKDAY_MINUTES:

        print("Current time:", clock, "minutes")

        if random.random() < 0.1 and len(tasks) > 0:
            print("New task incoming")
            if current is not None:
                workload.push(current)
            current = tasks.pop(0)

        if current is not None:
            current[1] -= 1
            print("Current task:", current[0], "(Time left:", current[1], "minutes)")
            if current[1] == 0:
                if not workload.is_empty():
                    current = workload.pop()
                else:
                    current = None
        else:
            print("No current task")
        

        print("Current stack:", workload)
        print("------------------------------------")

        clock += 1




def main():
    """Main function of the script."""
    WORKDAY_MINUTES = 60
    tasks = [ ['read work emails',10], \
          ['respond to emails', 10], \
          ['attend meeting', 15], \
          ['coffee break', 15], \
          ['talk to boss', 10], \
          ['read work emails',10], \
          ['respond to emails', 10], \
          ['conference call', 15], \
          ['conversation with colleague', 15], \
          ['coffee break', 15], \
          ['meet with student', 15] ]
    
    workday(tasks, WORKDAY_MINUTES)

if __name__ == "__main__":
    main()