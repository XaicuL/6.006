# Enqueue(Q, x)

# Q[Q.tail] = x
# if Q.tail == Q.length
#     Q.tail = 1
# else Q.tail = Q.tail + 1

# Dequeue(Q)

# x = Q[Q.head]
# if Q.head == Q.length
#     Q.head = 1
# else Q.head = Q.head + 1
# return x

class Queue:
    def __init__(self, n):
        self.length = n
        self.Q = [None] * (n + 1)  # 1-based처럼 쓰기 위함
        self.head = 1
        self.tail = 1

    def empty(self):
        return self.head == self.tail

    def enqueue(self, x):
        # overflow: tail 다음 칸이 head면 가득 참 (칸 하나 비워 둠)
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
