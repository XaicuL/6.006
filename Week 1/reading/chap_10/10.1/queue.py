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
    def __init__(self, n): #self는 클래스 자기 자신을 가리킴, n은 큐의 크기
        self.length = n #length는 큐의 크기
        self.Q = [None] * (n + 1)  # 1-based처럼 쓰기 위함
        self.head = 1 #head는 큐의 맨 앞을 가리킴
        self.tail = 1 #tail는 큐의 맨 뒤를 가리킴

    def empty(self):
        return self.head == self.tail #head가 tail과 같으면 True를 반환

    def enqueue(self, x):
        # overflow: tail 다음 칸이 head면 가득 참 (칸 하나 비워 둠) #overflow 오류 발생
        next_tail = 1 if self.tail == self.length else self.tail + 1 #next_tail은 tail+1이면 tail+1, 아니면 1
        if next_tail == self.head:
            raise Exception("overflow") #overflow 오류 발생
        self.Q[self.tail] = x
        self.tail = next_tail #tail을 next_tail로 설정

    def dequeue(self):
        if self.empty():
            raise Exception("underflow") #underflow 오류 발생
        x = self.Q[self.head] #Q의 head번째 원소를 x로 설정
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
q.enqueue(17) #17을 큐에 삽입
q.enqueue(3) #3을 큐에 삽입
print(f"head={q.head}, tail={q.tail}") #head와 tail을 출력
print(f"dequeue(3): {q.dequeue()}")  # 9을 큐에서 삭제
