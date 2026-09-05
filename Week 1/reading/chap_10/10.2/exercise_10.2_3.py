class Node:
    def __init__(self, key): #self는 클래스 자기 자신을 가리킴, key는 노드의 키
        self.key = key
        self.next = None #next는 다음 노드를 가리킴


class Queue:
    def __init__(self):
        self.front = None #front는 큐의 맨 앞을 가리킴
        self.rear = None #rear는 큐의 맨 뒤를 가리킴

    # O(1)
    def enqueue(self, key):
        node = Node(key) #node는 key를 가진 노드

        if self.rear is None:
            self.front = self.rear = node #front와 rear를 node로 설정
            return

        self.rear.next = node #rear의 next를 node로 설정
        self.rear = node #rear를 node로 설정

    # O(1)
    def dequeue(self):
        if self.front is None: #front이 None이면 None을 반환
            return None

        value = self.front.key
        self.front = self.front.next #front를 front의 next로 설정

        if self.front is None:
            self.rear = None #rear를 None으로 설정

        return value #value를 반환

    def print_queue(self):
        cur = self.front #cur을 front로 설정
        while cur:
            print(cur.key, end=" ")
            cur = cur.next #cur을 cur의 next로 설정
        print()
