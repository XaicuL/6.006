#Stack - Empty(S)

# if S.top == 0
#     return True
# else return False

# Push(S, x)

# S.top = S.top + 1
# S[S.top] = x

#Pop(S)

# if Stack-empty(S)
#     error "underflow"
# else S.top S.top - 1
#     return S[S.top + 1]

# s = [15, 6, 2, 9]

# s.append(17)
# print(f'last in(1) : {s[len(s) - 1]}')#17
# print(f's length(1) = {len(s)}')


# s.append(3)
# print(f'last in(2) : {s[len(s) - 1]}')#3
# print(f's length(2) = {len(s)}')


# pop_s = s.pop()
# print(f'last in(3) : {s[len(s) - 1]}') #17


class Stack:
    def __init__(self, n):
        self.S = [None] * (n + 1)  # 1-based처럼 쓰기 위함
        self.top = 0

    def empty(self):
        return self.top == 0

    def push(self, x):
        self.top += 1
        self.S[self.top] = x

    def pop(self):
        if self.empty():
            raise Exception("underflow")
        self.top -= 1
        return self.S[self.top + 1]


s = Stack(7)
for x in [15, 6, 2, 9]:
    s.push(x)
print(f"top after init: {s.S[s.top]}")  # 9

s.push(17)
print(f"top after push(17): {s.S[s.top]}")  # 17
print(f"top index(1): {s.top}")

s.push(3)
print(f"top after push(3): {s.S[s.top]}")  # 3
print(f"top index(2): {s.top}")

popped = s.pop()
print(f"popped: {popped}")  # 3
print(f"top after pop: {s.S[s.top]}")  # 17
print(f"top index(3): {s.top}")
