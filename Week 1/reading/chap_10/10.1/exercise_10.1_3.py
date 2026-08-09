class ArrayQueue:
    def __init__(self, n):
        self.Q = [None] * n
        self.length = n
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        self.Q[self.tail] = x
        self.tail = 0 if self.tail == self.length - 1 else self.tail + 1

    def dequeue(self):
        x = self.Q[self.head]
        self.head = 0 if self.head == self.length - 1 else self.head + 1
        return x

    def show(self, label):
        print(f"{label:15s} Q={self.Q} head={self.head} tail={self.tail}")

Q = ArrayQueue(6)
Q.show("초기상태")
Q.enqueue(4); Q.show("ENQUEUE(Q,4)")
Q.enqueue(1); Q.show("ENQUEUE(Q,1)")
Q.enqueue(3); Q.show("ENQUEUE(Q,3)")
val = Q.dequeue(); print(f"  -> DEQUEUE 반환값: {val}"); Q.show("DEQUEUE(Q)")
Q.enqueue(8); Q.show("ENQUEUE(Q,8)")
val = Q.dequeue(); print(f"  -> DEQUEUE 반환값: {val}"); Q.show("DEQUEUE(Q)")
