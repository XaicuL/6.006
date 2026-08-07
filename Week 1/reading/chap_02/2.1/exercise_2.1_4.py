# Input: n-bit integers A[1..n] and B[1..n], each element in {0, 1}
# Output: (n+1)-element array C[1..n+1] storing the sum A + B in binary
#
# carry = 0
# for i = 1 to n
#     x = A[i] + B[i] + carry
#     C[i] = x mod 2
#     carry = floor(x / 2)
# C[n + 1] = carry
# return C

A = [1, 1, 0, 1]   # 1011 (LSB at index 0)
B = [0, 1, 1, 0]   # 0110
n = len(A)
C = [0] * (n+1)

carry = 0

for i in range(n):
    C[i] = A[i] + B[i] + carry
    carry = C[i] // 2
    C[i] = C[i] % 2

C[n] = carry

print(C)
