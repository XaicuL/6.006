# n1 = q - p + 1 : p부터 q까지의 원소 개수
# n2 = r - q : q부터 r까지의 원소 개수

# let L[1..n1+1] and R[1..n2+1] be new arrays : n1 + 1개의 원소와 n2 + 1개의 원소를 가진 새로운 배열
# for i = 1 to n1 : n1개의 원소를 순회
#     L[i] = A[p + i - 1] : p부터 q까지의 원소를 L 배열에 저장
# for j = 1 to n2 : n2개의 원소를 순회
#     R[j] = A[q + j] : q부터 r까지의 원소를 R 배열에 저장
# L[n1 + 1] = ∞ : L 배열의 마지막 원소에 무한대 값 저장
# R[n2 + 1] = ∞ : R 배열의 마지막 원소에 무한대 값 저장
# i = 1 : L 배열의 첫 번째 원소 인덱스
# j = 1 : R 배열의 첫 번째 원소 인덱스
# for k = p to r : p부터 r까지의 원소를 순회
#     if L[i] <= R[j] : L 배열의 원소가 R 배열의 원소보다 작거나 같으면
#         A[k] = L[i] : L 배열의 원소를 A 배열에 저장
#         i = i + 1 : L 배열의 인덱스 증가

def merge(A, p, q, r):
    n1 = q - p + 1 # n1 은 q - p + 1 로 Assign
    n2 = r - q # n2 은 r - q 로 Assign

    L = [0] * (n1 + 1) # Array name : L , Assign : 첫번째 element 부터 n1 + 1 개의 원소를 가진 배열을 생성
    R = [0] * (n2 + 1) # Array name : R , Assign : 첫번째 element 부터 n2 + 1 개의 원소를 가진 배열을 생성

    for i in range(n1): # loop variable : i , range : 1 to n1
        L[i] = A[p + i - 1] #L[i] 에 A[p + i - 1] 을 Assign
        """
        Ex)
        i = 1 일때 라고 가정
        L[1] = A[p + 1 - 1] = A[p] = A[1]

        i = 2 일때 라고 가정
        L[2] = A[p + 2 - 1] = A[p + 1] = A[2]

        i = 10 일때 라고 가정
        L[10] = A[p + 10 - 1] = A[p + 9] = A[10]

        => L[i] 는 A[p + i - 1] 을 Assign 하게 됨 -> 즉, L[i] 는 A[p] 부터 A[p + i - 1] 까지의 원소를 가진 배열을 생성하게 됨
        """

    for j in range(n2): # loop variable : j , range : 1 to n2
        R[j] = A[q + j] #R[j] 에 A[q + j] 을 Assign
        """
        Ex)
        j = 1 일때 라고 가정
        R[1] = A[q + 1] = A[q + 1] = A[2]

        j = 2 일때 라고 가정
        R[2] = A[q + 2] = A[q + 2] = A[3]

        j = 10 일때 라고 가정
        R[10] = A[q + 10] = A[q + 10] = A[11]

        => R[j] 는 A[q + j] 을 Assign 하게 됨 -> 즉, R[j] 는 A[q] 부터 A[q + j] 까지의 원소를 가진 배열을 생성하게 됨
        """
    L[n1 + 1] = float('inf') # L 배열의 마지막 원소에 무한대 값 저장
    R[n2 + 1] = float('inf') # R 배열의 마지막 원소에 무한대 값 저장

    i = 1 # i 는 1로 Assign
    j = 1 # j 는 1로 Assign
