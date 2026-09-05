class Queue:
    def __init__(self, n): #self는 클래스 자기 자신을 가리킴, n은 큐의 크기
        self.length = n #length는 큐의 크기
        self.Q = [None] * (n + 1) #Q는 list, n+1개의 None을 가짐
        self.head = 1 #head는 큐의 맨 앞을 가리킴
        self.tail = 1 #tail는 큐의 맨 뒤를 가리킴

    def empty(self):
        return self.head == self.tail #head가 tail과 같으면 True를 반환

    def enqueue(self, x):
        next_tail = 1 if self.tail == self.length else self.tail + 1 #next_tail은 tail+1이면 tail+1, 아니면 1
        if next_tail == self.head:
            raise Exception("overflow") #overflow 오류 발생
        self.Q[self.tail] = x #Q의 tail번째 원소를 x로 설정
        self.tail = next_tail #tail을 next_tail로 설정

    def dequeue(self):
        if self.empty():
            raise Exception("underflow") #underflow 오류 발생
        x = self.Q[self.head]
        if self.head == self.length:
            self.head = 1 #head를 1로 설정
        else:
            self.head += 1 #head를 1 증가
        return x #x를 반환


q = Queue(6)
for x in [15, 6, 9, 8, 4]:
    q.enqueue(x)
print(f"dequeue(1): {q.dequeue()}")  # 15
print(f"dequeue(2): {q.dequeue()}")  # 6
q.enqueue(17)
q.enqueue(3)
print(f"head={q.head}, tail={q.tail}")
print(f"dequeue(3): {q.dequeue()}")  # 9
