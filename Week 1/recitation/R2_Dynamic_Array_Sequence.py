class Dynamic_Array_Seq(Array_Seq):
    def __init__(self): #self는 클래스 자기 자신을 가리킴, capacity는 list의 용량, r는 용량 증가 비율
        super().__init__()
        self.capacity = 0 #capacity는 list의 용량
        self.r = r #r는 용량 증가 비율
        self._compute_bounds() #_compute_bounds()는 용량 증가 비율을 계산
        self.resize(0) #resize(0)은 용량을 0으로 설정

        def __len__(self):
            return self.size #self.size를 반환

    def __iter__(self):
        for i in range(len(self)): #i는 0부터 len(self)까지 반복
            yield self.A[i] #self.A의 i번째 원소를 반환

    def build(self, X):
        for a in X: #X를 순회
            self.insert_last(a) #a를 삽입

    def _compute_bounds(self):
        self.upper = len(self.A) #self.A의 길이를 upper로 설정
        self.lower = len(self.A) // (self.r * self.r) #self.A의 길이를 lower로 설정

    def _resize(self, n):
        if (self.lower < n < self.upper): return
        m = max(n , 1) * self.r #m은 n과 1 중 큰 값을 r로 곱한 값
        A = [None] * m #A는 list, m개의 None을 가짐
        self._copy_forward(0, len(self), 0, A, 0)
        self.A = A #self.A를 A로 설정
        self._compute_bounds() #_compute_bounds()는 용량 증가 비율을 계산

    def insert_last(self, x):
        self._resize(self.size + 1) #self.size + 1을 용량으로 설정
        self.A[self.size] = x #self.A의 self.size번째 원소를 x로 설정
        self.size += 1

    def delete_last(self):
        self.A[self.size - 1] = None #self.A의 self.size-1번째 원소를 None으로 설정
        self.size -= 1 #self.size를 1 감소
        self._resize(self.size) #self.size를 용량으로 설정

    def insert_at(self, i, x):
        self.insert_last(None) #None을 삽입
        self._copy_backward(i, self.size - i - 1, self.A, i + 1) #i부터 self.size-i-1까지 self.A의 i+1번째 원소를 복사
        self.A[i] = x #self.A의 i번째 원소를 x로 설정

    def delete_at(self, i):
        x = self.A[i] #self.A의 i번째 원소를 x로 설정
        self._copy_forward(i + 1, self.size - (i + 1), self.A, i) #i+1부터 self.size-(i+1)까지 self.A의 i번째 원소를 복사
        self.delete_last() #마지막 원소를 삭제
        return x

    def insert_first(self, x):
        self.insert_at(0, x) #0번째 위치에 x를 삽입

    def delete_first(self):
        return self.delete_at(0) #0번째 위치의 원소를 삭제


