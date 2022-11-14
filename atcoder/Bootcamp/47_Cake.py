"""
ケーキの切り分け２ (Cake 2)
https://www.ioi-jp.org/joi/2014/2015-ho/2015-ho-t2-review.pdf (Ref1)
https://kakedashi-engineer.appspot.com/2020/05/16/joi2015hob/ (Ref2)

これはきちんと読めるようにするを目標にする.
おそらくRef1で愚直に実装するとTLEする.
Ref2で最後からの切るパターンをループで考える.

方針
・dp[l][r]:=残り[l,r]となった状態で、JOIくんの取り分合計が最大となる場合の値

更新
次の式では、i<jとなる(区間の大小)
(i)  JOIくんのターンの時 (好きな方、選べる)
dp[i][j] = max(dp[i+1][j]+A[i], dp[i][j-1]+A[j])

(ii) IOIくんのターンの時 (大きい方を必ず選ぶ)
dp[i][j] = dp[i+1][j]+A[i] (A[i]>A[j])
dp[i][j] = dp[i][j-1]+A[j] (A[i]<A[j])

JOIくんの取り分合計が最大になるようにする

dp表
----------------
     j=0 j=1 j=2 j=3 j=4
i=0   0   0   0   0   0 
i=1   0   0   0   0   0 
i=2   0   0   0   0   0 
i=3   0   0   0   0   0 
i=4   0   0   0   0   0 
----------------
→ dpも1次元で考えた方が楽っぽい

N=5
---
 2 id=0
 8 id=1
 1 id=2
10 id=3
 9 id=4
 --------円環対策として、同じものを2回並べる
 2 id=5
 8 id=6
 1 id=7
10 id=8
 9 id=9
---
18
               2  8  1 10  9  2  8  1 
               ↓
->  dp[0][3]   2  8  1 10       
    dp[1][4]      8  1 10  9
    dp[2][5]         1 10  9  2
    dp[3][6]           10  9  2  8
    dp[4][7]               9  2  8  1
"""
import numpy as np

N = int(input())
l = []

for i in range(N):
    l.append(int(input()))

A = np.array(l)
A = np.concatenate([A,A])

dp = np.zeros(N,np.int64)

# 残りのピースがd個あるとして計算していく
for d in range(1,N+1):
    dp = np.append(dp,dp[0]) #dp = [0,0,0,0,0,0]
    player = (N-d)&1 # Nが奇数なら最後はJOI
    if player==0:
        #JOI
        left  = dp[1:N+1] + A[:N]     # [0,0,0,0]+[8,1,10,9] = [8,1,10,9] (del 2)
        right = dp[:N] + A[d-1:N+d-1] # [0,0,0,0]+[2,8,1,10] = [2,8,1,10] (del 9)
        dp = np.maximum(left,right)   # [ 8,  8, 10, 10]
    else:
        dp = np.where(A[:N] > A[d-1:N+d-1], dp[1:N+1], dp[:N])
answer = dp.max()
print(answer)