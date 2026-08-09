class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.nil = Node(None)
        self.head = self.nil

    def insert(self, key):
        node = Node(key)
        node.next = self.head
        self.head = node

    def search(self, k):
        self.nil.key = k      # Sentinel

        x = self.head
        while x.key != k:
            x = x.next

        if x == self.nil:
            return None

        return x
