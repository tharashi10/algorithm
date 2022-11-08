"""
こちらの問題に切り替え
https://atcoder.jp/contests/dp/tasks/dp_c

自力でACできた
添え字利用のDP
3
10 40 70
20 50 80
30 60 90
210
"""
n = int(input())
A = []
for i in range(n):
    A.append(list(map(int,input().split())))

#dp[i][j]:= i-1日までの間で、i-1日の活動がkとなる場合の、最大幸福度 (k=0,1,2)
#dp[i+1][k]:= dp[i][j] + A[][]
#dp[3][0]= dp[i][j] + A[i][0] j=1 or 2(連続した活動はできない制約があるため)

dp = []
for i in range(n+1):
    dp.append([0]*3)

for i in range(n):   # i日目
    for j in range(3): # j=0,1,2
        for k in range(3): # k=0,1,2
            if k != j:
                #print(f"k,j= {k},{j}")
                dp[i+1][k] = max(dp[i+1][k], dp[i][j] + A[i][k])

#for i in range(n+1):
#    print(*dp[i])

print(max(dp[n]))
#print(dp)
