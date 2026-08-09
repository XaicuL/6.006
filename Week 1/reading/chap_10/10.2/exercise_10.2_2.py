class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # O(1)
    def push(self, key):
        node = Node(key)
        node.next = self.top
        self.top = node

    # O(1)
    def pop(self):
        if self.top is None:
            raise IndexError("Stack is empty")

        value = self.top.key
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            return None
        return self.top.key

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        curr = self.top
        while curr:
            print(curr.key, end=" -> ")
            curr = curr.next
        print("None")

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # O(1)
    def push(self, key):
        node = Node(key)
        node.next = self.top
        self.top = node

    # O(1)
    def pop(self):
        if self.top is None:
            raise IndexError("Stack is empty")

        value = self.top.key
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            return None
        return self.top.key

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        curr = self.top
        while curr:
            print(curr.key, end=" -> ")
            curr = curr.next
        print("None")

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.print_stack()
# 30 -> 20 -> 10 -> None

print(stack.pop())   # 30
print(stack.peek())  # 20

stack.print_stack()
# 20 -> 10 -> None
