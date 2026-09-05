class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def reverse(head):

    prev = None #prev을 None으로 설정
    curr = head #curr을 head로 설정

    while curr:
        nxt = curr.next #nxt을 curr의 next로 설정
        curr.next = prev
        prev = curr #prev을 curr로 설정
        curr = nxt #curr을 nxt로 설정

    return prev #prev을 반환
