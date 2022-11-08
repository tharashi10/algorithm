"""
方針: 添え字DP
初期条件にて、誤ってdp[1][k](1日目時点で服Kを着た時の最大派手さ)に値を入れない
あくまでもDPの定義は、|Ci-Ci+1|...的な差分値の最大を表すので1日目自体の初期条件は全て0である
3 4
31
27
35
20 25 30
23 29 90
21 35 60
28 33 40

服 4種類
Day1   Day2   Day3
-------------------
31度   27度    35度
-------------------
服0は、20<T<25 で最適で、派手さは30
服1は、23<T<29 で最適で、派手さは90
服2は、21<T<35 で最適で、派手さは60
服3は、28<T<33 で最適で、派手さは40

"""

n, m = map(int,input().split())
T = [0]
for i in range(n):
    T.append(int(input()))

l = []
for i in range(m):
    l.append(list(map(int,input().split())))

# dpは日にちを扱うので、1-Indexedとする
dp = []
for i in range(n+1):
    dp.append([-10**6 for _ in range(m)])

# dp[n][m]:= d日目に服nを着た場合のMAX派手スコア　と定義する

# 初期条件
for k in range(m):
    dp[0][k]=0
    dp[1][k]=0

for i in range(2,n+1): # n日目の時のMAXを出したい
    for j in range(m): # m種類の服 服Jを選ぶとする
        for k in range(m): # m種類の服 一つ前
            ## ここの最初のステップでT[1]を参照して判定Checkを行わなかったのがいけなかった....
            if i==2:
                if l[j][0]<=T[i]<=l[j][1] and l[k][0]<=T[1]<=l[k][1]:
                    dp[i][j] = max(dp[i][j],dp[i-1][k]+abs(l[j][2]-l[k][2]))
            else:
                if l[j][0]<=T[i]<=l[j][1]:
                    dp[i][j] = max(dp[i][j],dp[i-1][k]+abs(l[j][2]-l[k][2]))

print(max(dp[n]))