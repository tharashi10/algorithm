"""
自力で行けた
最小コインの枚数
15 6
1 2 7 8 12 50
--
2
"""

S, N = map(int,input().split())
coins = [0]+list(map(int,input().split()))
dp = []
for i in range(N+1):
    dp.append([0 for _ in range(S+1)])

for k in range(S+1):
    dp[0][k] = 10**5

for j in range(1,N+1):
    for s in range(1,S+1):
        if s-coins[j]>=0:
            dp[j][s]=min(dp[j][s-coins[j]]+1,dp[j-1][s])
        else:
            dp[j][s]=dp[j-1][s]

candidate = []
for i in range(1,N+1):
    candidate.append(dp[i][S])
print(min(candidate))