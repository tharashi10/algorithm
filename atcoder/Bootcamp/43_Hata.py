"""
パ研軍旗
--Input
3
WWR
#RW
BW#
##B
RBR
--Output
10
"""

N = int(input())
A = []
for i in range(5):
    st = str(input())
    A.append([0] + [ st[j] for j in range(N)])

dp = []
# 行は3色
# 赤 dp[0]
# 青 dp[1]
# 白 dp[2]
for i in range(3):
    dp.append([10**10 for j in range(N+1)])

tmp_ini = []
for flg in range(5):
    tmp_ini.append(A[flg][1])

clist = ['R','B','W']

# 初期条件
dp[0][1] = 5-tmp_ini.count(clist[0])
dp[1][1] = 5-tmp_ini.count(clist[1])
dp[2][1] = 5-tmp_ini.count(clist[2])

for i in range(2,N+1):
    tmp_i = []
    for flg in range(5):
        tmp_i.append(A[flg][i])
    
    for j in range(3):
        for jj in range(3):
            if j!=jj:
                dp[j][i] = min(dp[j][i],dp[jj][i-1]+(5-tmp_i.count(clist[j])))

ans = 10*10
for i in range(3):
    ans = min(ans,dp[i][N])

print(ans)