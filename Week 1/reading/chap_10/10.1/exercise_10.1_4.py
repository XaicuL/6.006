class Queue:
    def __init__(self, n):
        self.length = n
        self.Q = [None] * (n + 1) 
        self.head = 1
        self.tail = 1

    def empty(self):
        return self.head == self.tail

    def enqueue(self, x):
        next_tail = 1 if self.tail == self.length else self.tail + 1
        if next_tail == self.head:
            raise Exception("overflow")
        self.Q[self.tail] = x
        self.tail = next_tail

    def dequeue(self):
        if self.empty():
            raise Exception("underflow")
        x = self.Q[self.head]
        if self.head == self.length:
            self.head = 1
        else:
            self.head += 1
        return x


q = Queue(6)
for x in [15, 6, 9, 8, 4]:
    q.enqueue(x)
print(f"dequeue(1): {q.dequeue()}")  # 15
print(f"dequeue(2): {q.dequeue()}")  # 6
q.enqueue(17)
q.enqueue(3)
print(f"head={q.head}, tail={q.tail}")
print(f"dequeue(3): {q.dequeue()}")  # 9
