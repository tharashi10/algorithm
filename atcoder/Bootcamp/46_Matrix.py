"""
方針:
・dp[i][j]:=dp[開始位置][終了位置]

Matrix Chain Multiplication
6
30 35
35 15
15 5
5 10
10 20
20 25
---
15125

"""
import itertools

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))

ll = list(itertools.chain.from_iterable(l))

mat=[]
for i in range(n*2):
    if i<=1:
        mat.append(ll[i])
    else:
        if i%2==1:
            mat.append(ll[i])
# mat=[30, 35, 15, 5, 10, 20, 25]

INF = float('inf')
dp = []
for i in range(n+1):
    dp.append([INF for j in range(n+1)])

for i in range(n):
    dp[i][i+1] = 0

for i in range(n+1):
    for j in range(i+1,n+1):
        for k in range(i+1,j-i):
            print(f"mat:{mat}")
            print(f"[i={i},j={j},k={k}]")
            dp[i][j] = min(dp[i][j], dp[i][i+k]+dp[i+k][j]+mat[i]*mat[k]*mat[j])

print(dp)
