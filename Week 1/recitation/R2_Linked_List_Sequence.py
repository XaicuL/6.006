from re import X


class Linked_list_Node:
    def __init__(self, x): #self는 클래스 자기 자신을 가리킴, x는 원소
        self.item = x
        self.next = None #next는 다음 노드를 가리킴

    def later_node(self, i):
        if i == 0: #i가 0이면
            return self
        assert next #next가 None이 아니면 오류 발생
        return self.next.later_node(i - 1) #self.next의 i-1번째 노드를 반환

class Linked_list_Seq:
    def __init__(self): #self는 클래스 자기 자신을 가리킴, head는 첫 노드를 가리킴, size는 리스트의 크기
        self.head = None #head는 첫 노드를 가리킴
        self.size = 0 #size는 리스트의 크기

    def __len__(self):
        return self.size #size를 반환

    def __iter__(self):
        node = self.head #node는 첫 노드를 가리킴
        while node:
            yield node.item #node.item을 반환
            node = node.next

    def build(self, X):
        for a in reversed(X):
            self.insert_first(a) #a를 첫 노드에 삽입

    def get_at(self, i):
        node = self.head.later_node(i) #node는 첫 노드의 i번째 노드를 가리킴
        return node.item

def set_at(self, i, x):
    node = self.head.later_node(i) #node는 첫 노드의 i번째 노드를 가리킴
    node.item = x #node의 item을 x로 설정

def insert_first(self, x):
    new_node = Linked_list_Node(x)
    new_node.next = self.head #new_node의 next는 head를 가리킴
    self.head = new_node
    self.size += 1 #size를 1 증가

def delete_first(self):
    x = self.head.item #head의 item을 x로 설정
    self.head = self.head.next #head는 head의 next를 가리킴
    self.size -= 1
    return x #x를 반환

def insert_at(self, i, x):
    if i == 0: #i가 0이면
        self.insert_first(x) #x를 첫 노드에 삽입
        return
    now_node = Linked_list_Node(x) #now_node는 x를 가리킴
    node = self.head.later_node(i - 1) #node는 첫 노드의 i-1번째 노드를 가리킴
    new_node.next = node.next #new_node의 next는 node의 next를 가리킴
    node.next = new_node #node의 next는 new_node를 가리킴
    self.size += 1 #size를 1 증가

def delete_at(self, i):
    if i == 0: #i가 0이면
        return self.delete_first()
    node = self.head.later_node(i - 1) #node는 첫 노드의 i-1번째 노드를 가리킴
    x = node.next.item #node의 next의 item을 x로 설정
    node.next = node.next.next #node의 next는 node의 next의 next를 가리킴
    self.size -= 1 #size를 1 감소
    return x #x를 반환
