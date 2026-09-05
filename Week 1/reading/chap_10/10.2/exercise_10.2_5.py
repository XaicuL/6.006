class Node:
    def __init__(self, key): #self는 클래스 자기 자신을 가리킴, key는 노드의 키
        self.key = key
        self.next = None #next는 다음 노드를 가리킴


class CircularList:
    def __init__(self):
        self.head = None #head는 원형 리스트의 맨 앞을 가리킴

    def insert(self, key):
        node = Node(key) #node는 key를 가진 노드

        if self.head is None:
            self.head = node #head를 node로 설정
            node.next = node #node의 next를 node로 설정
            return

        node.next = self.head.next #node의 next를 head의 next로 설정
        self.head.next = node #head의 next를 node로 설정

    def search(self, key):
        if self.head is None: #head가 None이면 None을 반환
            return None #None을 반환

        cur = self.head #cur을 head로 설정

        while True:
            if cur.key == key:
                return cur #cur을 반환
            cur = cur.next #cur을 cur의 next로 설정
            if cur == self.head:
                break #cur이 head와 같으면 반복문 종료

        return None #None을 반환

    def delete(self, key):
        if self.head is None: #head가 None이면 None을 반환
            return #head가 None이면 None을 반환

        prev = self.head #prev을 head로 설정
        cur = self.head #cur을 head로 설정

        while True:

            if cur.key == key:

                if cur == self.head:

                    if self.head.next == self.head:
                        self.head = None #head를 None으로 설정
                        return

                    tail = self.head #tail을 head로 설정
                    while tail.next != self.head:
                        tail = tail.next #tail을 tail의 next로 설정

                    self.head = self.head.next #head를 head의 next로 설정
                    tail.next = self.head

                else:
                    prev.next = cur.next #prev의 next를 cur의 next로 설정

                return #head가 None이면 None을 반환

            prev = cur #prev을 cur로 설정
            cur = cur.next #cur을 cur의 next로 설정

            if cur == self.head:
                break #cur이 head와 같으면 반복문 종료
