class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def reverse(head):

    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev
