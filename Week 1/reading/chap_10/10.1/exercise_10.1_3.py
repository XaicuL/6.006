class ArrayQueue:
    def __init__(self, n): #self는 클래스 자기 자신을 가리킴, n은 큐의 크기
        self.Q = [None] * n
        self.length = n #length는 큐의 크기
        self.head = 0 #head는 큐의 맨 앞을 가리킴
        self.tail = 0 #tail는 큐의 맨 뒤를 가리킴

    def enqueue(self, x):
        self.Q[self.tail] = x #Q의 tail번째 원소를 x로 설정
        self.tail = 0 if self.tail == self.length - 1 else self.tail + 1 #tail을 1 증가

    def dequeue(self):
        x = self.Q[self.head] #Q의 head번째 원소를 x로 설정
        self.head = 0 if self.head == self.length - 1 else self.head + 1 #head을 1 증가
        return x #x를 반환

    def show(self, label):
        print(f"{label:15s} Q={self.Q} head={self.head} tail={self.tail}") #label을 15자리로 출력, Q는 Q의 원소를 출력, head는 head를 출력, tail는 tail을 출력

Q = ArrayQueue(6)
Q.show("초기상태") #초기상태를 출력
Q.enqueue(4); Q.show("ENQUEUE(Q,4)")
Q.enqueue(1); Q.show("ENQUEUE(Q,1)") #ENQUEUE(Q,1)를 출력
Q.enqueue(3); Q.show("ENQUEUE(Q,3)") #ENQUEUE(Q,3)를 출력
val = Q.dequeue(); print(f"  -> DEQUEUE 반환값: {val}"); Q.show("DEQUEUE(Q)")
Q.enqueue(8); Q.show("ENQUEUE(Q,8)") #ENQUEUE(Q,8)를 출력
val = Q.dequeue(); print(f"  -> DEQUEUE 반환값: {val}"); Q.show("DEQUEUE(Q)")
 #DEQUEUE(Q)를 출력
