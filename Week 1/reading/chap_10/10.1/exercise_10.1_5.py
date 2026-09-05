class Deque:
    def __init__(self, capacity): #self는 클래스 자기 자신을 가리킴, capacity는 덱의 크기
        self.capacity = capacity #capacity는 덱의 크기
        self.arr = [None] * capacity #arr는 list, capacity개의 None을 가짐
        self.front = 0 #front는 덱의 맨 앞을 가리킴
        self.size = 0 #size는 덱의 크기

    # Insert at the FRONT
    def insert_front(self, value):
        if self.size == self.capacity:
            raise OverflowError("Deque is full") #overflow 오류 발생

        self.front = (self.front - 1) % self.capacity #front를 front-1로 설정
        self.arr[self.front] = value #arr의 front번째 원소를 value로 설정
        self.size += 1 #size를 1 증가

    # Insert at the REAR
    def insert_rear(self, value):
        if self.size == self.capacity:
            raise OverflowError("Deque is full") #overflow 오류 발생

        rear = (self.front + self.size) % self.capacity #rear를 front+size로 설정
        self.arr[rear] = value #arr의 rear번째 원소를 value로 설정
        self.size += 1 #size를 1 증가

    # Delete from the FRONT
    def delete_front(self):
        if self.size == 0:
            raise IndexError("Deque is empty") #index 오류 발생

        value = self.arr[self.front] #arr의 front번째 원소를 value로 설정
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity #front를 front+1로 설정
        self.size -= 1 #size를 1 감소
        return value #value를 반환

    # Delete from the REAR
    def delete_rear(self):
        if self.size == 0:
            raise IndexError("Deque is empty") #index 오류 발생

        rear = (self.front + self.size - 1) % self.capacity #rear를 front+size-1로 설정
        value = self.arr[rear] #arr의 rear번째 원소를 value로 설정
        self.arr[rear] = None #arr의 rear번째 원소를 None으로 설정
        self.size -= 1 #size를 1 감소
        return value #value를 반환

# Test code

dq = Deque(5)

# Insert at rear
dq.insert_rear(10) #10을 덱의 뒤에 삽입
dq.insert_rear(20) #20을 덱의 뒤에 삽입
dq.insert_rear(30) #30을 덱의 뒤에 삽입

print("Delete front:", dq.delete_front())   # 10을 덱의 앞에서 삭제

# Insert at front
dq.insert_front(5) #5을 덱의 앞에 삽입
dq.insert_front(1) #1을 덱의 앞에 삽입

# Current deque: 1, 5, 20, 30

print("Delete front:", dq.delete_front())   # 1을 덱의 앞에서 삭제
print("Delete rear:", dq.delete_rear())     # 30

# Insert again at both ends
dq.insert_front(0)
dq.insert_rear(40)

# Current deque: 0, 5, 20, 40

print("Delete front:", dq.delete_front())   # 0
print("Delete rear:", dq.delete_rear())     # 40
print("Delete front:", dq.delete_front())   # 5
print("Delete rear:", dq.delete_rear())     # 20
