class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0
        self.size = 0

    # Insert at the FRONT
    def insert_front(self, value):
        if self.size == self.capacity:
            raise OverflowError("Deque is full")

        self.front = (self.front - 1) % self.capacity
        self.arr[self.front] = value
        self.size += 1

    # Insert at the REAR
    def insert_rear(self, value):
        if self.size == self.capacity:
            raise OverflowError("Deque is full")

        rear = (self.front + self.size) % self.capacity
        self.arr[rear] = value
        self.size += 1

    # Delete from the FRONT
    def delete_front(self):
        if self.size == 0:
            raise IndexError("Deque is empty")

        value = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    # Delete from the REAR
    def delete_rear(self):
        if self.size == 0:
            raise IndexError("Deque is empty")

        rear = (self.front + self.size - 1) % self.capacity
        value = self.arr[rear]
        self.arr[rear] = None
        self.size -= 1
        return value

# Test code

dq = Deque(5)

# Insert at rear
dq.insert_rear(10)
dq.insert_rear(20)
dq.insert_rear(30)

print("Delete front:", dq.delete_front())   # 10

# Insert at front
dq.insert_front(5)
dq.insert_front(1)

# Current deque: 1, 5, 20, 30

print("Delete front:", dq.delete_front())   # 1
print("Delete rear:", dq.delete_rear())     # 30

# Insert again at both ends
dq.insert_front(0)
dq.insert_rear(40)

# Current deque: 0, 5, 20, 40

print("Delete front:", dq.delete_front())   # 0
print("Delete rear:", dq.delete_rear())     # 40
print("Delete front:", dq.delete_front())   # 5
print("Delete rear:", dq.delete_rear())     # 20
