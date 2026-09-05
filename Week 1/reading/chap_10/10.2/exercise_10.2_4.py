class Node:
    def __init__(self, key): #self는 클래스 자기 자신을 가리킴, key는 노드의 키
        self.key = key
        self.next = None #next는 다음 노드를 가리킴


class LinkedList:
    def __init__(self): #self는 클래스 자기 자신을 가리킴
        self.nil = Node(None) #nil은 None을 가진 노드
        self.head = self.nil #head를 nil로 설정

    def insert(self, key): #self는 클래스 자기 자신을 가리킴, key는 노드의 키
        node = Node(key) #node는 key를 가진 노드
        node.next = self.head
        self.head = node #head를 node로 설정

    def search(self, k): #self는 클래스 자기 자신을 가리킴, k는 노드의 키
        self.nil.key = k      # Sentinel #nil의 key를 k로 설정

        x = self.head #x를 head로 설정
        while x.key != k:
            x = x.next #x를 x의 next로 설정

        if x == self.nil:
            return None #x가 nil이면 None을 반환

        return x #x를 반환
