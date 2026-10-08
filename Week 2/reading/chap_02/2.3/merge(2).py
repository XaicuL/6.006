# if p < r: : p가 r보다 작으면
#     q = floor((p + r) / 2) : q는 p와 r의 중간 인덱스
#     merge_sort(A, p, q) : A 배열의 p부터 q까지를 정렬
#     merge_sort(A, q + 1, r) : A 배열의 q + 1부터 r까지를 정렬
#     merge(A, p, q, r) : A 배열의 p부터 r까지를 병합

def merge_sort(A, p, r):
    if p < r:
        q = floor((p+r) / 2)
        """
        Ex)
        p = 1, r = 10 일때
        q = floor((1 + 10) / 2) = 5
        """
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        """
        Ex)
        p = 1, q = 5, r = 10 일때
        merge_sort(A, 6, 10) : A 배열의 6부터 10까지를 정렬
        """
        merge(A, p, q, r)
        """
        Ex)
        p = 1, q = 5, r = 10 일때
        merge(A, 1, 5, 10)
        """

