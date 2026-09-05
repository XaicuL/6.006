# for i = 1 to A.length
#     if A[i] == v
#         return i
# return NIL

def linear_search(A, v): #A는 list, v는 찾고자 하는 값, return은 찾고자 하는 값의 인덱스
    for i in range(len(A)): #i는 0부터 len(A)까지 반복
        if A[i] == v:
            return i #A[i]가 v와 같으면 i 반환
    return None #A[i]가 v와 같지 않으면 None 반환

A = [31, 41, 59, 26, 41, 58]
v = 26
result = linear_search(A, v)
print(result)
