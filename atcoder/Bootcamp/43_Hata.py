"""
パ研軍旗
・やはりdp書けば解ける.
・「こいつ」と書いたところ、10*10で計算してACせず1時間くらいはまった...前回も同じ感じでやってしまったのに
---dp
10000000000 4 8 10
10000000000 4 8 11
10000000000 4 7 12

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
    A.append([0] + [st[j] for j in range(N)])

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
        tmp_i.append(A[flg][i]) # tmp_i = ['R','#','#','B','W']
    
    for key in range(3):
        cdict = {0:'R',1:'B',2:'W'}
        pp = cdict.pop(key) # ex. key=0の時、cdict={1:'B',2:'W'},pp=R
        jj = [int(k) for k,v in cdict.items()]
        
        dp[key][i] = min(dp[jj[0]][i-1],dp[jj[1]][i-1])+(5-tmp_i.count(pp))

ans = 10**10 #こいつ
for i in range(3):
    ans = min(ans,dp[i][N])

print(ans)