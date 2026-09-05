# for i = 1 to n-1
#     min = i
#     for j = i+1 to n
#         if A[j] < A[min]
#             min = j
#     swap A[i] and A[min]

A = [3, 1, 4, 2, 5, 9]

for i in range(len(A)-1): #i는 0부터 len(A)-1까지 반복
    min = i
    for j in range(i+1, len(A)): #j는 i+1부터 len(A)까지 반복
        if A[j] < A[min]: #A[j]가 A[min]보다 작으면
            min = j #min을 j로 변경
    A[i], A[min] = A[min], A[i] #A[i]와 A[min]을 교환

print(A)

