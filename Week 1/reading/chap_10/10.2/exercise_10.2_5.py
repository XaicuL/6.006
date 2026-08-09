class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None

    def insert(self, key):
        node = Node(key)

        if self.head is None:
            self.head = node
            node.next = node
            return

        node.next = self.head.next
        self.head.next = node

    def search(self, key):
        if self.head is None:
            return None

        cur = self.head

        while True:
            if cur.key == key:
                return cur
            cur = cur.next
            if cur == self.head:
                break

        return None

    def delete(self, key):
        if self.head is None:
            return

        prev = self.head
        cur = self.head

        while True:

            if cur.key == key:

                if cur == self.head:

                    if self.head.next == self.head:
                        self.head = None
                        return

                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next

                    self.head = self.head.next
                    tail.next = self.head

                else:
                    prev.next = cur.next

                return

            prev = cur
            cur = cur.next

            if cur == self.head:
                break
