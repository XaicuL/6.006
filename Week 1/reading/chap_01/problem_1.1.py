import math

def log2(n): #function name : log2, input : n(int), output : math.log(n) / math.log(2)
    return math.log(n) / math.log(2) #math.log(n) : n의 자연로그, math.log(2) : 2의 자연로그

complexities = [lambda n: math.sqrt(n), #lambda n: math.sqrt(n) : n의 제곱근
                lambda n: n,
                lambda n: n * log2(n), #lambda n: n * log2(n) : n의 자연로그 * n
                lambda n: n ** 2, #lambda n: n ** 2 : n의 제곱
                lambda n: n ** 3, #lambda n: n ** 3 : n의 세제곱
                lambda n: 2 ** n,
                lambda n: math.factorial(n)]

max_bound = [1e40, 1e20, 1e20, 1e10, 1e10, 100, 100]

times = [1000 * 1000, #1000 * 1000 : 1000의 제곱
         1000 * 1000 * 60, #1000 * 1000 * 60 : 1000의 제곱 * 60
         1000 * 1000 * 60 * 60, #1000 * 1000 * 60 * 60 : 1000의 제곱 * 60 * 60
         1000 * 1000 * 60 * 60 * 24, #1000 * 1000 * 60 * 60 * 24 : 1000의 제곱 * 60 * 60 * 24
         1000 * 1000 * 60 * 60 * 24 * 30, #1000 * 1000 * 60 * 60 * 24 * 30 : 1000의 제곱 * 60 * 60 * 24 * 30
         1000 * 1000 * 60 * 60 * 24 * 365, #1000 * 1000 * 60 * 60 * 24 * 365 : 1000의 제곱 * 60 * 60 * 24 * 365
         1000 * 1000 * 60 * 60 * 24 * 365 * 100] #1000 * 1000 * 60 * 60 * 24 * 365 * 100 : 1000의 제곱 * 60 * 60 * 24 * 365 * 100

print(' '.join(map(lambda v: '2^(' + '{:.2e}'.format(v) + ')', times))) #' '.join(map(lambda v: '2^(' + '{:.2e}'.format(v) + ')', times)) : 2^(1e40) 2^(1e20) 2^(1e20) 2^(1e10) 2^(1e10) 2^(100) 2^(100)

for k in range(len(complexities)): #loop variable : k, range 는 complexities 라는 list의 길이만큼 진행
    """
    Ex)
    complexities[0] = lambda n: math.sqrt(n)

    complexities[1] = lambda n: n

    complexities[2] = lambda n: n * log2(n)

    ... etc

    if) complexities[k] 가 lambda n: math.sqrt(n) 일 때,
    complexities[k](mid) = math.sqrt(mid)

    if) complexities[k] 가 lambda n: n 일 때,
    complexities[k](mid) = mid

    if) complexities[k] 가 lambda n: n * log2(n) 일 때,
    complexities[k](mid) = mid * log2(mid)
    """
    c = complexities[k] #c = complexities[k] : complexities[k] 라는 함수를 c 라는 variable에 assign
    vals = [] #vals = [] : vals 라는 list를 initialize
    """
    Why initialize vals?
    초기화를 진행해야 하는 이유는 초기화를 진행하지 않으면 vals 라는 list에 값이 들어가지 않기 때문이다.
    """
    for t in times:
        l, r = 0, int(max_bound[k])
        """
        l, r = 0, int(max_bound[k]) : l = 0, r = int(max_bound[k]) : max_bound[k] 라는 list의 k번째 원소를 int로 변환하여 r 라는 variable에 assign
        """
        max_n = 0 #max_n = 0 : max_n 라는 variable을 0으로 initialize
        """
        Why initialize max_n?
        max_n 라는 variable을 0으로 initialize 하는 이유는 max_n 라는 variable을 0으로 initialize 하지 않으면 max_n 라는 variable에 값이 들어가지 않기 때문이다.
        """
        while l <= r: #l <= r 일 때 까지 반복하며 조건을 만족하는 값을 찾음
            mid = (l + r) // 2 #l = 0, r = int(max_bound[k]) 일 때, mid = (0 + int(max_bound[k])) // 2 : mid 라는 variable에 (0 + int(max_bound[k])) // 2 의 값을 assign
            val = c(mid) #c = complexities[k] 일 때, val = c(mid) : complexities[k] 라는 함수를 mid 라는 variable에 적용하여 val 라는 variable에 assign
            if val == float('inf') or val > t: #val == float('inf') or val > t : val 라는 variable이 float('inf') 보다 크거나 같을 때 그리고 val 라는 variable이 t 보다 클 때
                r = mid - 1
                """
                r = mid - 1 : r 라는 variable에 mid - 1 의 값을 assign
                """
            else:
                """
                else: : l = mid + 1, max_n = max(max_n, mid) : l 라는 variable에 mid + 1 의 값을 assign, max_n 라는 variable에 max(max_n, mid) 의 값을 assign
                """
                l = mid + 1
                """
                l = mid + 1 : l 라는 variable에 mid + 1 의 값을 assign
                """
                max_n = max(max_n, mid)
                """
                max_n = max(max_n, mid) : max_n 라는 variable에 max(max_n, mid) 의 값을 assign
                """
        vals.append(max_n)
    if k < 3: #k < 3 일 때
        """
        k < 3 일 때, vals 라는 list의 값을 '{:.2e}'.format(v) 의 형식으로 출력
        """
        print(' | '.join(map(lambda v: '{:.2e}'.format(v), vals)))
    else:
        """
        k >= 3 일 때, vals 라는 list의 값을 str(int(math.floor(v))) 의 형식으로 출력
        """
        print(' | '.join(map(lambda v: str(int(math.floor(v))), vals)))

#source: https://github.com/CyberZHG/CLRS/blob/master/Chapter_01_The_Role_of_Algorithms_in_Computing/problems.ipynb

