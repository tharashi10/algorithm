"""
方針:
・dp[i][j]:=dp[開始位置][終了位置]
・開区間にしなくてもよさそう
→ i番目~j番目までで、スカラーの計算量が最小となる計算量をDPとして定義.
・マストっぽいと書いた部分が一番むずくて、計算が合わなくなるところ

ABCの計算の場合,以下の2パターンある.
(i) (AB)C → (AB)の計算量 + (C)の計算量 (まだABCまとまった計算してないので) + alpha
(ii) A(CB) → (AB)の計算量 + (C)の計算量 (まだABCまとまった計算してないので) + alpha

alpha = M[0]*M[1]*M[]
↑alphaは、間の行数/列数がキャンセルされるので、結局最初（左と呼ぶ）と最後(右と呼ぶ)の
行数/列数で計算すればOK.

https://daily-tech.hatenablog.com/entry/2018/09/29/203935
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

4
3 2
2 3
3 1
1 2
--
18
"""
import itertools

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))

ll = list(itertools.chain.from_iterable(l))

m=[]
for i in range(n*2):
    if i<=1:
        m.append(ll[i])
    else:
        if i%2==1:
            m.append(ll[i])
# m=[30, 35, 15, 5, 10, 20, 25]

INF = float('inf')
dp = []
for i in range(n):
    dp.append([INF for j in range(n)])

for i in range(n):
    dp[i][i] = 0

# 更新の計算
for diff in range(1,n): # diff = j-i <--- マストっぽい
    for i in range(n-diff): # i=開始位置    j-i = diff
        j = diff+i
        for k in range(i,j): # diffをレンジにすることで、kがi基準のIndexになり得る
            #print(f"[i={i},j={j},k={k}]")
            dp[i][j] = min(dp[i][j], 
                           dp[i][k]+dp[k+1][j]+m[i]*m[k+1]*m[j+1])

#ABC
#k = 0,1
#i =0 j=2
#dp[0][1] = dp[0][0] + dp[0][1] + (m[0]*m[1]*m[2])
#dp[0][2] = dp[0][0] + dp[1][2] + (m[0]*m[1]*m[2])
#dp[0][2] = dp[0][1] + dp[2][2] + (m[0]*m[1]*m[2])
#dp[1][3] = dp[1][3] + dp[4][3] + (m[1]*m[3]*m[3]) NG
# BCD = (B)(CD) or (BC)(D)
#dp[1][3] = dp[1][1] + dp[2][3] + (m[1]*m[1]*m[3]) B(CD)
#dp[1][3] = dp[1][2] + dp[3][3] + (m[1]*m[2]*m[3]) BC(D)
print(dp[0][-1])
#i+k<j h<j-i
