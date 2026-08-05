# for j = 2 to A.length : 2번째 원소부터 끝까지 순회(1번째는 이미 정렬되었다 가정)
#     key = A[j] : 지금 끼워넣을 값
#     #Insert A[j] into the sorted sequence A[1..j-1] 
#     i = j - 1 : 정렬된 구간의 맨 끝부터 비교 시작
#     while i > 0 and A[i] > key: : key보다 큰 값이면 계속 왼쪽으로 이동 
#         A[i + 1] = A[i] : 큰 값을 한 칸 오른쪽으로 밀기
#         i = i - 1 : 왼쪽 원소로 이동
#     A[i + 1] = key : key를 알맞은 자리에 삽입

def insertion_sort(A): #function name : insertion_sort, input : A(list), output : A(list)
    for j in range(1, len(A)): #for j = 2 to A.length : 2번째 원소부터 끝까지 순회(1번째는 이미 정렬되었다 가정)
        """
        1부터 A라는 list의 길이 - 1 까지 순회를 함
        j는 loop variable이고, 2번째 원소부터 끝까지 순회를 함
        """

        """
        여기까지가 수학적 귀납법으로 가정한다면 base case에 해당
        (key 에 순회를 시작하기 전)
        """
        key = A[j] #key = A[j] : 지금 끼워넣을 값 
        """
        여기부터 
        Inductive step에 해당
        (key 에 순회를 시작한 후)
        """

        """
        key 라는 variable에  A[j] 를 assign 함
        단 A[j] 는 j 라는 loop variable이 2부터 순회를 하며 값이 변경되므로
        A 라는 list의 index를 가져오면 A[1] = 1번째 원소가 호출되어 오게 되고
        호출되어 온 원소가 key 라는 variable에 assign 되어 저장되게 됨
        """
        i = j - 1 #i = j - 1 : 정렬된 구간의 맨 끝부터 비교 시작
        """
        i 라는 variable은 j 라는 loop variable의 값을 1 빼서 정렬된 구간의 맨 끝부터 비교 시작
        Ex)
        j = 2 일 때, i = 1
        j = 3 일 때, i = 2
        j = 4 일 때, i = 3
        ...
        j = n 일 때, i = n - 1
        """

        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]

            """
        i 라는 variable이 0보다 크거나 같을때 그리고 A[i] 라는 원소가 key보다 클 때 까지 반복
        여기서 A[i] 란 i = j - 1 이었기에, key 라는 variable에 A[2] 가 오면
        A[i] = A[1] 이 되어 1번째 원소와 비교를 하게 됨
            """
            i -= 1
            """
            단 i 는 -1을 한 값을 re assign 하게 된다
            왜 사용했을까? 바로 다음 반복문에서 A[i + 1] = A[i] 를 하게 되므로
            """
        A[i + 1] = key

        """
        여기까지가 수학적 귀납법으로 가정한다면 inductive step에 해당
        (key 에 순회를 시작한 후)
        """
        
        """
        A[i+1] 이라는 variable에 key 라는 값을 assign하는데
        여기서 A[i+1] 이라는 값은 i는 반복을 하면 할수록 -1이 되어가므로
        A[i+1] = A[i] 를 하게 되면, A[i+1] = A[i-1] 이 되어 2번째 원소와 비교를 하게 됨
        """
    return A

A = [5, 2, 4, 6, 1, 3] #A 라는 list를 define AND Initialize
result = insertion_sort(A) #insertion_sort 함수를 호출하고 그 결과를 result 라는 variable에 assign
print(result) #result 라는 variable을 print 함

