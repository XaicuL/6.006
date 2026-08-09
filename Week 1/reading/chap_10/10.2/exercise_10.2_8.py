class XORNode:
    def __init__(self, key):
        self.key = key
        self.np = 0          # id(prev) XOR id(next)


class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        # id(node) -> node 객체를 찾기 위한 딕셔너리
        self.memory = {}

    def _id(self, node):
        return 0 if node is None else id(node)

    def _get(self, address):
        return None if address == 0 else self.memory.get(address)

    # O(1)
    def insert(self, key):
        node = XORNode(key)
        self.memory[id(node)] = node

        node.np = self._id(self.head)

        if self.head is not None:
            # head의 prev가 node로 바뀜
            self.head.np ^= self._id(node)
        else:
            self.tail = node

        self.head = node

    # O(n)
    def search(self, key):
        prev = None
        curr = self.head

        while curr:
            if curr.key == key:
                return curr

            nxt = self._get(curr.np ^ self._id(prev))
            prev, curr = curr, nxt

        return None

    # O(1)
    def delete(self, node):
        if node is None:
            return

        prev = None
        curr = self.head

        while curr != node:
            nxt = self._get(curr.np ^ self._id(prev))
            prev, curr = curr, nxt

        if curr is None:
            return

        nxt = self._get(curr.np ^ self._id(prev))

        # prev 수정
        if prev:
            prev_prev = self._get(prev.np ^ self._id(curr))
            prev.np = self._id(prev_prev) ^ self._id(nxt)
        else:
            self.head = nxt

        # next 수정
        if nxt:
            nxt_next = self._get(nxt.np ^ self._id(curr))
            nxt.np = self._id(prev) ^ self._id(nxt_next)
        else:
            self.tail = prev

        del self.memory[id(curr)]

    # O(1)
    def reverse(self):
        self.head, self.tail = self.tail, self.head

    def traverse(self):
        prev = None
        curr = self.head

        while curr:
            print(curr.key, end=" ")

            nxt = self._get(curr.np ^ self._id(prev))
            prev, curr = curr, nxt

        print()
