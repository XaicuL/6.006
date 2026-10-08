class staticArray:
    def __init__(self, n):
        self.data = [None] * n
    def get_at(self, i):
        if not (0 <= i < len(self.data)): raise IndexError
    def set_at(self, i, x):
        if not (0 <= i < len(self.data)): raise IndexError
        self.data[i] = x


def birthday_match(students):
    n = len(students) #students는 list, n은 students의 길이
    record = staticArray(n)

    for k in range(n): #k는 0부터 n까지 반복
        (name1, bday1) = students[k]
        for i in range(k): #i는 0부터 k까지 반복
            (name2, bday2) = record.get_at(i)
            if bday1 == bday2: #bday1이 bday2와 같으면
                return (name1, name2) #name1과 name2를 반환
        record.set_at(k, (name1, bday1)) #record의 k번째 원소를 (name1, bday1)로 설정
    return None
