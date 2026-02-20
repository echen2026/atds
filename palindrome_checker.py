#!/usr/bin/env python3

"""
palindrome_checker.py
Write a program palindrome_checker.py that includes a class definition for PalindromeChecker that includes at least two methods:
a setter method set_strict_mode() that takes a boolean value as input, which turns "strict mode" on and off
If "strict mode" is on, a palindrome will only be indicated if the phrase reads exactly the same, forwards and backwards, including spaces, punctuation, and case (upper and lower). If "strict mode" is off, then spaces, punctuation, and different cases are allowed, and the phrase will be identified as a palindrome because their letters all match.
a boolean method is_palindrome(phrase) that takes a phrase as a parameter and returns true if the phrase is a palindrome, and false if it isn't. This method should use a Deque object to check the expression, and return True if the expression entered is a valid palindrome.
You may wish to write an additional helper method sanitize(phrase) that will produce a new, "sanitized" version of a phrase that doesn't have any spaces, punctuation, or uppercase letters in it. This method can be useful when "strict mode" is off.

The main() function in the palindrome_checker.py can be used to perform a series of tests.
"""

__author__ = "Evan Chen"
__version__ = "2026-02-19"

import atds

strict_mode = False

def set_strict_mode(strict):
    global strict_mode
    if strict:
        strict_mode = True
    else:        
        strict_mode = False

def sanitize(phrase):
    new = ""
    for char in phrase:
        if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            new += char.lower()
    return new

def is_palindrome(phrase):
    if not strict_mode:
        phrase = sanitize(phrase)

    deque = atds.Deque()
    for char in phrase:
        deque.add_rear(char)

    while deque.size() >= 2:
        if deque.remove_front() != deque.remove_rear():
            return False

    return True


def main():
    """Main function of the script."""
    while True:
        print("------------------------------")
        print("Palindrome Checker")
        print("Do you want strict mode on or off? (on/off)")
        mode = input("Enter 'on' or 'off': ").lower()
        if mode == "on":
            set_strict_mode(True)
        elif mode == "off":
            set_strict_mode(False)
        else:
            print("Invalid input. Please enter 'on' or 'off'.")
            continue

        phrase = input("Enter a phrase: ")
        if is_palindrome(phrase):
            print(f"'{phrase}' is a palindrome. ({'Strict mode ON' if strict_mode else 'Strict mode OFF'})")
        else:
            print(f"'{phrase}' is not a palindrome. ({'Strict mode ON' if strict_mode else 'Strict mode OFF'})")
        

if __name__ == "__main__":
    main()