class XORNode:
    def __init__(self, key):
        self.key = key #key는 노드의 키
        self.np = 0          # id(prev) XOR id(next)


class XORLinkedList:
    def __init__(self): #self는 클래스 자기 자신을 가리킴
        self.head = None
        self.tail = None #tail은 오른쪽 노드를 가리킴

        # id(node) -> node 객체를 찾기 위한 딕셔너리
        self.memory = {} #memory는 노드의 객체를 찾기 위한 딕셔너리

    def _id(self, node):
        return 0 if node is None else id(node) #node가 None이면 0을 반환, 아니면 node의 id를 반환

    def _get(self, address):
        return None if address == 0 else self.memory.get(address) #address가 0이면 None을 반환, 아니면 address의 노드를 반환

    # O(1)
    def insert(self, key):
        node = XORNode(key) #node는 key를 가진 노드
        self.memory[id(node)] = node #memory에 node의 id를 키로 하고 node를 값으로 하는 딕셔너리

        node.np = self._id(self.head) #node의 np를 head의 id로 설정

        if self.head is not None:
            # head의 prev가 node로 바뀜
            self.head.np ^= self._id(node)
        else:
            self.tail = node #tail을 node로 설정

        self.head = node #head를 node로 설정

    # O(n)
    def search(self, key):
        prev = None #prev을 None으로 설정
        curr = self.head #curr을 head로 설정

        while curr:
            if curr.key == key: #curr의 key가 key와 같으면 curr을 반환
                return curr #curr을 반환

            nxt = self._get(curr.np ^ self._id(prev))
            prev, curr = curr, nxt #prev을 curr로, curr을 nxt로 설정

        return None #None을 반환

    # O(1)
    def delete(self, node):
        if node is None: #node가 None이면 None을 반환
            return #node가 None이면 None을 반환

        prev = None #prev을 None으로 설정
        curr = self.head #curr을 head로 설정

        while curr != node:
            nxt = self._get(curr.np ^ self._id(prev))
            prev, curr = curr, nxt #prev을 curr로, curr을 nxt로 설정

        if curr is None:
            return #curr가 None이면 None을 반환

        nxt = self._get(curr.np ^ self._id(prev))

        # prev 수정
        if prev: #prev가 None이 아니면
            prev_prev = self._get(prev.np ^ self._id(curr)) #prev_prev을 prev의 id와 curr의 id를 XOR 연산한 값으로 설정
            prev.np = self._id(prev_prev) ^ self._id(nxt) #prev의 np를 prev_prev의 id와 nxt의 id를 XOR 연산한 값으로 설정
        else: #prev가 None이면
            self.head = nxt #head를 nxt로 설정

        # next 수정
        if nxt: #nxt가 None이 아니면
            nxt_next = self._get(nxt.np ^ self._id(curr))
            nxt.np = self._id(prev) ^ self._id(nxt_next) #nxt의 np를 prev의 id와 nxt_next의 id를 XOR 연산한 값으로 설정
        else:
            self.tail = prev #tail을 prev로 설정

        del self.memory[id(curr)] #memory에서 curr의 id를 키로 하고 node를 값으로 하는 딕셔너리 삭제

    # O(1)
    def reverse(self):
        self.head, self.tail = self.tail, self.head #head를 tail로, tail을 head로 설정

    def traverse(self):
        prev = None #prev을 None으로 설정
        curr = self.head #curr을 head로 설정

        while curr:
            print(curr.key, end=" ") #curr의 key를 출력

            nxt = self._get(curr.np ^ self._id(prev))
            prev, curr = curr, nxt #prev을 curr로, curr을 nxt로 설정

        print() #줄바꿈
