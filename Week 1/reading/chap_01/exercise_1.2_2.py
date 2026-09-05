import math

n = (1, 8, 16, 32, 64, 128, 256, 512, 1024)


# print(math.log(4,2)) #밑이 2인 4의 로그

for i in n: # loop variable : i , n 내부를 순회하며 반복
    lhs = i/8 # left hand side
    rhs = math.log(i, 2) # right hand side

    if lhs < rhs: # 조건문 lhs < rhs 가 참이면 출력
        print(f'밑이 {i}일 때 => True')
    elif lhs > rhs: # 조건문 lhs > rhs 가 참이면 출력
        print(f'밑이 {i}일 때 => False')
