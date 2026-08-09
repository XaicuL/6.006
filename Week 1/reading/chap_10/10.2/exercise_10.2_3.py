class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # O(1)
    def enqueue(self, key):
        node = Node(key)

        if self.rear is None:
            self.front = self.rear = node
            return

        self.rear.next = node
        self.rear = node

    # O(1)
    def dequeue(self):
        if self.front is None:
            return None

        value = self.front.key
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value

    def print_queue(self):
        cur = self.front
        while cur:
            print(cur.key, end=" ")
            cur = cur.next
        print()
