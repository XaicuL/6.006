class ArrayStack:
    def __init__(self, n):
        self.S = [None] * n #S는 list, n개의 None을 가짐, n은 스택의 크기
        self.top = 0 #top은 스택의 맨 위를 가리킴

    def push(self, x):
        self.top += 1 #top을 1 증가
        self.S[self.top - 1] = x #S의 top-1번째 원소를 x로 설정

    def pop(self):
        x = self.S[self.top - 1] #S의 top-1번째 원소를 x로 설정
        self.top -= 1 #top을 1 감소
        return x

    def show(self, label):
        print(f"{label:15s} S={self.S} top={self.top}") #label을 15자리로 출력, S는 S의 원소를 출력, top은 top을 출력

S = ArrayStack(6)
S.show("초기상태") #초기상태를 출력
S.push(4); S.show("PUSH(S,4)")
S.push(1); S.show("PUSH(S,1)") #PUSH(S,1)를 출력
S.push(3); S.show("PUSH(S,3)") #PUSH(S,3)를 출력
val = S.pop(); print(f"  -> POP 반환값: {val}"); S.show("POP(S)")
S.push(8); S.show("PUSH(S,8)") #PUSH(S,8)를 출력
val = S.pop(); print(f"  -> POP 반환값: {val}"); S.show("POP(S)") #POP(S)를 출력
