class Node:
    def __init__(self, key): #self는 클래스 자기 자신을 가리킴, key는 노드의 키
        self.key = key
        self.next = None #next는 다음 노드를 가리킴


class Stack:
    def __init__(self):
        self.top = None #top은 스택의 맨 위를 가리킴

    # O(1)
    def push(self, key):
        node = Node(key) #node는 key를 가진 노드
        node.next = self.top
        self.top = node #top을 node로 설정

    # O(1)
    def pop(self):
        if self.top is None:
            raise IndexError("Stack is empty") #index 오류 발생

        value = self.top.key #top의 key를 value로 설정
        self.top = self.top.next #top을 top의 next로 설정
        return value #value를 반환

    def peek(self):
        if self.top is None: #top이 None이면 None을 반환
            return None
        return self.top.key

    def is_empty(self):
        return self.top is None #top이 None이면 True를 반환

    def print_stack(self):
        curr = self.top #curr을 top으로 설정
        while curr:
            print(curr.key, end=" -> ")
            curr = curr.next #curr을 curr의 next로 설정
        print("None")

class Node:
    def __init__(self, key):
        self.key = key #key는 노드의 키
        self.next = None #next는 다음 노드를 가리킴


class Stack:
    def __init__(self):
        self.top = None #top은 스택의 맨 위를 가리킴

    # O(1)
    def push(self, key):
        node = Node(key) #node는 key를 가진 노드
        node.next = self.top #node의 next를 top으로 설정
        self.top = node

    # O(1)
    def pop(self):
        if self.top is None:
            raise IndexError("Stack is empty") #index 오류 발생

        value = self.top.key #top의 key를 value로 설정
        self.top = self.top.next #top을 top의 next로 설정
        return value #value를 반환

    def peek(self):
        if self.top is None: #top이 None이면 None을 반환
            return None
        return self.top.key

    def is_empty(self):
        return self.top is None #top이 None이면 True를 반환

    def print_stack(self):
        curr = self.top #curr을 top으로 설정
        while curr:
            print(curr.key, end=" -> ")
            curr = curr.next #curr을 curr의 next로 설정
        print("None")

stack = Stack()

stack.push(10) #10을 스택에 삽입
stack.push(20) #20을 스택에 삽입
stack.push(30)
#30을 스택에 삽입

stack.print_stack()
# 30 -> 20 -> 10 -> None

print(stack.pop())   # 30
print(stack.peek())  # 20

stack.print_stack()
# 20 -> 10 -> None
