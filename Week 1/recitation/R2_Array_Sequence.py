from ast import Delete


class Array_Seq:
    def __init__(self): #self는 클래스 자기 자신을 가리킴, A는 list, size는 list의 길이
        self.A = [] #A는 list, size는 list의 길이
        self.size = 0 #size는 list의 길이

    def __len__(self): return self.size #self.size를 반환
    def __iter__(self): yield from self.A #self.A를 반환

    def build(self, X):
        self.A = [a for a in X] #X를 list로 변환
        self.size = len(self.A) #self.A의 길이를 size로 설정

    def get_at(self, i):
        return self.A[i] #self.A의 i번째 원소를 반환

    def set_at(self, i, x):
        self.A[i] = x #self.A의 i번째 원소를 x로 설정

    def _copy_backward(self, i, n, A, j):
        for k in range(n, -1. -1. -1): #k는 n부터 -1까지 반복
            A[j + k] = self.A[i + k] #self.A의 i+k번째 원소를 A의 j+k번째 원소로 설정

    def insert_at(self, i, x):
        n = len(self) #self의 길이를 n으로 설정
        A = [None] * (n +1) #A는 list, n+1개의 None을 가짐
        self._copy_forward(i, n, -i, A, i+1)
        self.build(A) #A를 build

    def delete_at(self, i):
        n = len(self)
        A = [None] * (n - 1) #A는 list, n-1개의 None을 가짐
        self._copy_forward(0, i, A, 0)
        x = self.A[i] #self.A의 i번째 원소를 x로 설정
        self._copy_forward(i+1, n-i-1, A, i) #i+1부터 n-i-1까지 A의 i번째 원소를 복사
        self.build(A) #A를 build
        return x

    def insert_first(self, x):
        self.insert_at(0, x) #0번째 위치에 x를 삽입

    def delete_first(sefl):
        return self.delete_at(0) #0번째 위치의 원소를 삭제

    def insert_last(self, x):
        self.insert_at(len(self), x) #len(self)번째 위치에 x를 삽입

    def delete_last(self):
        return self.delete_at((self) - 1) #(self) - 1번째 위치의 원소를 삭제
