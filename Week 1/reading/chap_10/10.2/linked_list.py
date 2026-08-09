#List-Search(L, k)

# x = L.head
# while x != NIL and x.key != k
#     x = x.next
# return x

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, k):
        x = self.head

        while x is not None and x.key != k:
            x = x.next

        return x

L = LinkedList()

L.head = Node(1)
L.head.next = Node(4)
L.head.next.next = Node(9)
L.head.next.next.next = Node(16)

x = L.search(9)
print(f"key: {x.key}")

#List-Insert(L, x)

# x.next = L.head
# if L.head != NIL
#     L.head.prev = x
# L.head = x
# x.prev = NIL

def insert(self, x):
    x.next = self.head
    if self.head is not None:
        self.head.prev = x
    self.head = x
    x.prev = None


def print_list(L):
    x = L.head
    keys = []
    while x is not None:
        keys.append(x.key)
        x = x.next
    print(f"list: {keys}")


L2 = LinkedList()

insert(L2, Node(16))
print(f"head after insert(16): {L2.head.key}")
print(f"head.prev is None: {L2.head.prev is None}")
print_list(L2)  # [16]

insert(L2, Node(9))
insert(L2, Node(4))
insert(L2, Node(1))
print_list(L2)  # [1, 4, 9, 16]

print(f"head.prev is None: {L2.head.prev is None}")
print(f"second node prev: {L2.head.next.prev.key}")  # 1
print(f"second node key: {L2.head.next.key}")  # 4

found = L2.search(9)
print(f"search(9): {found.key}")
print(f"search(99) is None: {L2.search(99) is None}")

#List-Delete(L, x)
# if x.prev != NIL
#     x.prev.next = x.next
# else
#     L.head = x.next
# if x.next != NIL
#     x.next.prev = x.prev

def delete(self, x):
    if x.prev is not None:
        x.prev.next = x.next
    else:
        self.head = x.next
    if x.next is not None:
        x.next.prev = x.prev
    return x


L3 = LinkedList()

L3.head = Node(16)
L3.head.next = Node(9)
L3.head.next.next = Node(4)
L3.head.next.next.next = Node(1)

delete(L3, L3.head.next)
print_list(L3)  # [1, 4, 16]

delete(L3, L3.head)
print_list(L3)  # [4, 16]

#List-Delete'(L, x)

# x.prev.next = x.next
# x.next.prev = x.prev

def delete_prime(self, x):
    if x.prev is not None:
        x.prev.next = x.next
    else:
        self.head = x.next
    if x.next is not None:
        x.next.prev = x.prev
    return x

L4 = LinkedList()

L4.head = Node(16)
L4.head.next = Node(9)
L4.head.next.next = Node(4)
L4.head.next.next.next = Node(1)

delete_prime(L4, L4.head.next)
print_list(L4)  # [1, 4, 16]

delete_prime(L4, L4.head)
print_list(L4)  # [4, 16]

#List-search'(L,k)

# while x != L.nil and x.key != k:
#     x = x.next
# return x

def search_prime(self, k):
    x = self.head
    while x is not None and x.key != k:
        x = x.next
    return x

L5 = LinkedList()

L5.head = Node(16)
L5.head.next = Node(9)
L5.head.next.next = Node(4)
L5.head.next.next.next = Node(1)

x = search_prime(L5, 9)
print(f"key: {x.key}")

x = search_prime(L5, 10)
print(f"key: {x is None}")

#List-insert'(L, x)

# x.next = L.nil.next
# L.nil.next = x
# x.prev = L.nil

def insert_prime(self, x):
    x.next = self.head
    if self.head is not None:
        self.head.prev = x
    self.head = x
    x.prev = None

L6 = LinkedList()

L6.head = Node(16)
L6.head.next = Node(9)
L6.head.next.next = Node(4)
L6.head.next.next.next = Node(1)

insert_prime(L6, Node(10))
print_list(L6)  # [1, 4, 9, 10, 16]


