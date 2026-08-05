# for i = 1 to A.length
#     if A[i] == v
#         return i
# return NIL

def linear_search(A, v):
    for i in range(len(A)):
        if A[i] == v:
            return i
    return None

A = [31, 41, 59, 26, 41, 58]
v = 26
result = linear_search(A, v)
print(result)