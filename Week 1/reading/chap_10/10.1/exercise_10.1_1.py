class ArrayStack:
    def __init__(self, n):
        self.S = [None] * n
        self.top = 0 

    def push(self, x):
        self.top += 1
        self.S[self.top - 1] = x

    def pop(self):
        x = self.S[self.top - 1]
        self.top -= 1
        return x

    def show(self, label):
        print(f"{label:15s} S={self.S} top={self.top}")

S = ArrayStack(6)
S.show("초기상태")
S.push(4); S.show("PUSH(S,4)")
S.push(1); S.show("PUSH(S,1)")
S.push(3); S.show("PUSH(S,3)")
val = S.pop(); print(f"  -> POP 반환값: {val}"); S.show("POP(S)")
S.push(8); S.show("PUSH(S,8)")
val = S.pop(); print(f"  -> POP 반환값: {val}"); S.show("POP(S)")
