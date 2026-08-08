#Stack - Empty(S)

# if S.top == 0
#     return True
# else return False

# Push(S, x)

# S.top = S.top + 1
# S[S.top] = x

#Pop(S)

# if Stack-empty(S)
#     error "underflow"
# else S.top S.top - 1
#     return S[S.top + 1]

s = [15, 6, 2, 9]

s.append(17)
print(f'last in(1) : {s[len(s) - 1]}')#17
print(f's length(1) = {len(s)}')


s.append(3)
print(f'last in(2) : {s[len(s) - 1]}')#3
print(f's length(2) = {len(s)}')


pop_s = s.pop()
print(f'last in(3) : {s[len(s) - 1]}') #17


