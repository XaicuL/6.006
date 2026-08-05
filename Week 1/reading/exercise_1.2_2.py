import math

n = (1, 8, 16, 32, 64, 128, 256, 512, 1024)


# print(math.log(4,2)) #밑이 2인 4의 로그 

for i in n:
    lhs = i/8
    rhs = math.log(i, 2)

    if lhs < rhs:
        print(f'밑이 {i}일 때 => True')
    elif lhs > rhs:
        print(f'밑이 {i}일 때 => False')