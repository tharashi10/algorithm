"""
Knapsack
#35 との違いは,「何回も製品を選べること」
→ 一般ナップザックと呼ぶ(重複OKなので)
→ 漸化式にて、左上を参照するのではなく、同一行の左側を参照するように変更する

4 8
4 2
5 2
2 1
8 3
21
"""

N,W = map(int,input().split())
value = [0]
weight = [0]
for i in range(N):
    v,w= map(int,input().split())
    weight.append(w)
    value.append(v)

# dpテーブル: 製品数i×容量j
dp = [[-1]*(W+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(W+1):
        dp[i][j]=0

for i in range(1,N+1):
    v = value[i]
    w = weight[i]
    
    for j in range(W+1):
        if j-w>=0:
            dp[i][j] = max(dp[i][j-w]+v,dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

#[print(dp[i]) for i in range(N+1)]
print(dp[N][W])

