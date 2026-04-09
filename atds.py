#!/usr/bin/env python3

"""
atds.py
Advanced Topics Data Structures
A collection of data types for the Advanced Topics class.
"""

__author__ = "Evan Chen"
__version__ = "2026-02-12"

class HashTable():
    def __init__(self, m):
        self.m = m
        self.entries = 0
        self.keys = m*[None]
        self.values = m*[None]

    def __repr__(self):
        return "Keys: " + str(self.keys) + "\nValues: " + str(self.values)
    
    def hash_function(self, key, m):
        return key % m
    
    def __len__(self):
        return self.entries
    
    def put(self, key, value):
        # Tries to put the key and value in their appropriate locations in the slots and keys arrays. If the key is already in the hash table, the new value replaces the current value, and if the calculated hash location is already occupied by a different value, a linear probe is conducted to place the key-value pair in an appropriate position.
        hash = self.hash_function(key, self.m)
        while self.keys[hash] != None and self.keys[hash] != key:
            hash = (hash + 1) % self.m
        if self.keys[hash] == None:
            self.entries += 1
        self.keys[hash] = key
        self.values[hash] = value
        

    def get(self, key):
        # Returns the value associated with the key, or None if the value doesn't exist in the hash table.
        hash = self.hash_function(key, self.m)
        while self.keys[hash] != None and self.keys[hash] != key:
            hash = (hash + 1) % self.m
        if self.keys[hash] == key:
            return self.values[hash]
        return None


class LinearSearcher():
    def search(self, list, int):
        for i in range(len(list)):
            if list[i] == int:
                return i
        return None

class BinarySearcher():
    """Binary searches a sorted list"""
    def search(self, list, num):
        low = 0
        high = len(list) - 1
        while low <= high:
            mid = (low + high) // 2
            if list[mid] == num:
                return mid
            elif list[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
        return None
    
class BinarySearcherRecursive():
    """recursively Binary searches a sorted list"""
    def search(self, arr : list, value : int) -> int:
        if len(arr) == 0:
            return None
        mid = len(arr) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            ret = BinarySearcherRecursive.search(self, arr[mid+1:], value)
            if ret is not None:
                return mid + 1 + ret
            else:
                return None
        else:
            return BinarySearcherRecursive.search(self, arr[:mid], value)


class ULStack():
    """A stack implemented using an UnorderedList"""
    def __init__(self):
        self.uls = UnorderedList()

    def push(self, item):
        self.uls.add(item)

    def peek(self):
        item = self.uls.pop()
        self.uls.add(item)
        return item
    
    def pop(self):
        return self.uls.pop(0)

    def size(self):
        return self.uls.length()
    
    def is_empty(self):
        return self.uls.is_empty()
    
    def __str__(self):
        return str(self.uls)

class UnorderedList():
    """Maintains an unordered list via a linked series of Nodes"""
    def __init__(self):
        self.head = None

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def length(self):
        node_count = 0
        current = self.head
        while current != None:
            node_count += 1
            current = current.get_next()
        return node_count
    
    def is_empty(self):
        return self.head == None
    
    def remove(self, item):
        previous = None
        current = self.head
        while current != None:
            if current.get_data() == item:
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                return
            else:
                previous = current
                current = current.get_next()    
        return
    
    def search(self, item):
        current = self.head
        while current != None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()
        return False
    
    def append(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_node)

    def index(self, item):
        count = 0
        current = self.head
        while current != None:
            if current.get_data() == item:
                return count
            else:
                current = current.get_next()
                count += 1

    def insert(self, pos, item):
        new_node = Node(item)
        if pos == 0:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            previous = None
            current = self.head
            count = 0
            while current != None and count < pos:
                previous = current
                current = current.get_next()
                count += 1
            previous.set_next(new_node)
            new_node.set_next(current)

    def pop(self, pos=None):
        if pos is None:
            pos = self.length() - 1
        if pos == 0:
            if self.head != None:
                item = self.head.get_data()
                self.head = self.head.get_next()
                return item
        else:
            previous = None
            current = self.head
            count = 0
            while current != None and count < pos:
                previous = current
                current = current.get_next()
                count += 1
            if current != None:
                item = current.get_data()
                previous.set_next(current.get_next())
                return item
        return None

    

    def __repr__(self):
        """Creates a representation of the list suitable for printing,
        debugging.
        """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result
    

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
    """testing searchers"""
    list1 = [1, 2, 3, 4, 7, 9, 13, 14, 20]
    search1 = 7
    search2 = 1
    search3 = 20
    search4 = -2
    search5 = 23
    search6 = 10
    list2 = [4, 7, 9, 13, 14, 20]
    search7 = 9
    search8 = 13
    search9 = 20
    search10 = 2
    search11 = 10
    search12 = 22

    linear_searcher = BinarySearcherRecursive()
    print(linear_searcher.search(list1, search1))
    print(linear_searcher.search(list1, search2))
    print(linear_searcher.search(list1, search3))
    print(linear_searcher.search(list1, search4))
    print(linear_searcher.search(list1, search5))
    print(linear_searcher.search(list1, search6))
    print(linear_searcher.search(list2, search7))
    print(linear_searcher.search(list2, search8))
    print(linear_searcher.search(list2, search9))
    print(linear_searcher.search(list2, search10))
    print(linear_searcher.search(list2, search11))
    print(linear_searcher.search(list2, search12))

if __name__ == "__main__":
    main()
