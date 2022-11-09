"""
方針:
・m日目に、都市iにいた場合の最小疲労度をdp[i][m]とおく。
・求めたい最小疲労度は、dp[N][1],dp[N][2],.....dp[N][M]の最も小さい疲労度となる。
→ dp[N][M]

3 5
10
25
15
50
30
15
40
30
--
1125
"""
N, M = map(int,input().split())
DIST = []
C = []

for i in range(N):
    DIST.append(int(input()))
for j in range(M):
    C.append(int(input()))

dp = [[10**6]*(M+1) for i in range(N+1)]
dp[0][0] = 0

for i in range(1,N+1):
    #dp[i][m] = dp[i][m-1] # 待機する場合
    #dp[i][m] = dp[i-1][m-1] + CLIM[m-1]*DIST[i-1] # 進める場合
    for m in range(i,M-N+i+1):
        dp[i][m] = min(dp[i][m-1],dp[i-1][m-1]+C[m-2]*DIST[i-2])
        
#for i in range(N+1):
#    print(*dp[i])
#print(C)
print(min(dp[N]))
#dp[1][] = dp[0][] + c[0]*d[0]

