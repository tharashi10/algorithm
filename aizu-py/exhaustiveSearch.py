def solve(i,m):
    if m == 0:
        return True
    if i > N:
        return False
    result = solve(i+1,m) or solve(i,A[i]-m)
    return result

N = int(input())
A = [int(input()) for _ in range(N)]
M = int(input())
m = [int(input()) for _ in range(M)]

for i in range(len(m)):
    if solve(i,m[i]):
        print('yes')
    else:
        print('no')    