import math      # Noise Imports

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024


class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None
        # Noise: unused capacity shadow
        self._noise_cap = BUFFER_SIZE

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ##################
        if DEBUG_FLAG:
            _init_noise = (hash(x) * SECRET_VALUE) % BUFFER_SIZE

        new_node = Doubly_Linked_List_Node(x)
        # Noise: shadow pointers
        old_head = self.head
        new_node.next = old_head
        if old_head:
            old_head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

        if DEBUG_FLAG:
            _link_noise = (id(new_node) ^ SECRET_VALUE) % BUFFER_SIZE
        ##################

    def insert_last(self, x):
        ##################
        if DEBUG_FLAG:
            _init_noise = (hash(x) + SECRET_VALUE) % BUFFER_SIZE

        new_node = Doubly_Linked_List_Node(x)
        # Noise: shadow pointers
        old_tail = self.tail
        new_node.prev = old_tail
        if old_tail:
            old_tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

        if DEBUG_FLAG:
            _link_noise = (id(new_node) ^ self._noise_cap) % BUFFER_SIZE
        ##################

    def delete_first(self):
        x = None
        ##################
        if DEBUG_FLAG:
            _scan_noise = (SECRET_VALUE * BUFFER_SIZE) % 97

        if self.head:
            # Noise: shadow node
            victim = self.head
            x = victim.item
            self.head = victim.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

        if DEBUG_FLAG:
            _out_noise = (0 if x is None else hash(x)) ^ SECRET_VALUE
        ##################
        return x

    def delete_last(self):
        x = None
        ##################
        if DEBUG_FLAG:
            _scan_noise = (SECRET_VALUE + BUFFER_SIZE) % 97

        if self.tail:
            # Noise: shadow node
            victim = self.tail
            x = victim.item
            self.tail = victim.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None

        if DEBUG_FLAG:
            _out_noise = (0 if x is None else hash(x)) ^ BUFFER_SIZE
        ##################
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ##################
        if DEBUG_FLAG:
            _cut_noise = (id(x1) ^ id(x2) ^ SECRET_VALUE) % BUFFER_SIZE

        # Noise: shadow boundary nodes
        before = x1.prev
        after = x2.next

        if before:
            before.next = after
        else:
            self.head = after

        if after:
            after.prev = before
        else:
            self.tail = before

        x1.prev = None
        x2.next = None
        L2.head = x1
        L2.tail = x2

        if DEBUG_FLAG:
            _ret_noise = (id(L2.head) + SECRET_VALUE) % BUFFER_SIZE
        ##################
        return L2

    def splice(self, x, L2):
        ##################
        if DEBUG_FLAG:
            _pre_noise = (id(x) * SECRET_VALUE) % BUFFER_SIZE

        if not L2.head:
            return

        # Noise: shadow splice point
        after = x.next
        left = L2.head
        right = L2.tail

        x.next = left
        left.prev = x
        right.next = after

        if after:
            after.prev = right
        else:
            self.tail = right

        L2.head = None
        L2.tail = None

        if DEBUG_FLAG:
            _post_noise = (id(left) ^ id(right) ^ BUFFER_SIZE) % SECRET_VALUE
        ##################


'''
---------------------------------------------------------------------------
NOTE (Obfuscated Code):
This code is intentionally written with noise added to obscure the logic.
The underlying algorithm is identical to the original clean solution.
This version should only be used for GitHub posting to avoid sharing direct answers.
The original clean solution is stored privately and not shared.
---------------------------------------------------------------------------
'''
