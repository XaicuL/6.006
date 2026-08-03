class StaticArray:
    def __init__(self, n):
        self.data = [None] * n

    def get_at(self, i):
        return self.data[i]

    def set_at(self, i, x):
        self.data[i] = x


print("---OCW---")

def birthday_math(students):
    n = len(students) #len : O(1) operation
    database = StaticArray(n) #Size of the array is O(n)
    #필요한 이유 : 인터뷰한 학생들의 (이름, 생일) 기록이 저장 할 공간이 필요하기 때문

    for k in range(n): #학생을 순서대로 인터뷰함 -> O(n) operation
        (name1, bday1) = students[k] #학생의 이름과 생일을 가져옴 -> O(1) operation

        for i in range(k): #이전에 인터뷰한 학생들과 비교함 -> O(n) operation
            (name2, bday2) = database.get_at(i) #이전에 인터뷰한 학생의 이름과 생일을 가져옴 -> O(1) operation

            if bday1 == bday2: #생일이 같은 학생이 있는 경우 -> O(1) operation
                return (name1, name2) #두 학생의 이름을 반환 -> O(1) operation

        database.set_at(k, (name1, bday1)) #학생의 이름과 생일을 데이터베이스에 저장 -> O(1) operation
    return None #모든 학생을 인터뷰했는데 생일이 같은 학생이 없는 경우 -> O(1) operation

