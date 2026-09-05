def insertion_sort(A): #decreasing order
    for j in range(1, len(A)): #loop variable : j , range는 1부터 len(A) 까지 반복 , A는 list이므로 len(A)는 list의 길이
        key = A[j]
        i = j - 1 #i는 j-1로 초기화

        while i >= 0 and A[i] < key: #A[i]가 key보다 작을 때까지 반복
            A[i + 1] = A[i] #A[i+1]에 A[i] 저장
            i -= 1 #i를 1 감소
        A[i + 1] = key #A[i+1]에 key 저장

    return A

A = [31, 41, 59, 26, 41, 58]
result = insertion_sort(A)
print(result)

#source : https://stackoverflow.com/questions/53561425/how-to-do-insertion-sort-with-a-decreasing-range

#i = j - 1로 변경 -> 정렬된 구간의 맨 끝부터 비교 시작
# while i >= 0 and A[i] < key: 로 변경 -> key보다 작은 값이 나올 때까지 비교
