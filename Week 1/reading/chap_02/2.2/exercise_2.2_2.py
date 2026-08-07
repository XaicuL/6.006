# for i = 1 to n-1
#     min = i
#     for j = i+1 to n
#         if A[j] < A[min]
#             min = j
#     swap A[i] and A[min]

A = [3, 1, 4, 2, 5, 9]

for i in range(len(A)-1):
    min = i
    for j in range(i+1, len(A)):
        if A[j] < A[min]:
            min = j
    A[i], A[min] = A[min], A[i]

print(A)

