def insertion_sort(A): 
    for j in range(1, len(A)):
        key = A[j] 
        i = j - 1

        while i >= 0 and A[i] < key:
            A[i + 1] = A[i]

            i -= 1
        A[i + 1] = key


    return A

A = [31, 41, 59, 26, 41, 58]
result = insertion_sort(A)
print(result)

#source : https://stackoverflow.com/questions/53561425/how-to-do-insertion-sort-with-a-decreasing-range

#i = j - 1로 변경 -> 정렬된 구간의 맨 끝부터 비교 시작
# while i >= 0 and A[i] < key: 로 변경 -> key보다 작은 값이 나올 때까지 비교