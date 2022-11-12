"""
・ノーマルDP最後の問題(結構飽きてきたから早くbitDPや区間DPに行きたいというのが正直な感想..)
・方針
・dp[i][j]: i番目の入力信号で、複合後の出力信号がjとなる時の、二乗和の最小と定義する
・例
入力信号X = [131,137]
コードブロックA = [-4,-2,-1,0,1,2,4]
コードブロックA[4]を選んだとする ; next_j = j + A[4]
dp[2][133] = min( dp[2][133], dp[1][132]+(133-X[0])^2 )

・TLEになるけど、解法としては正しいのでこのままOKとする。
Input--
2 7
4
2
1
0
-1
-2
-4
131
137
2 7
4
2
1
0
-1
-2
-4
131
123
10 7
-4
-2
-1
0
1
2
4
132
134
135
134
132
128
124
122
121
122
5 1
255
0
0
0
0
0
4 1
0
255
0
255
0
0 0
-- Output
2
8
0
325125
65026

"""

ans=[]
while True:
    n,m = map(int,input().split()) #n:Input, m:CodeBlock
    if n==0 and m==0:
        break
    C = []
    for i in range(m):
        C.append(int(input()))
    
    X = []
    for i in range(n):
        X.append(int(input()))

    INF = float('inf')
    dp = []
    for i in range(n+1):
        dp.append([INF]*256)
    dp[0][128] = 0

    for ii in range(1,n+1):
        for j in range(256):
            for l in range(m):
                jj = j + C[l]
                jj = max(0,min(255,jj))
                #print(f"ii,jj,l= {ii},{jj},{l}")
                dp[ii][jj]=min(dp[ii][jj], dp[ii-1][j]+(jj-X[ii-1])**2)

    #print(min(dp[n]))
    ans.append(min(dp[n][:]))

for k in range(len(ans)):
    print(ans[k])
