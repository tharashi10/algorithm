"""
方針:
・m日目に、都市iにいる場合の最小疲労度をdp[i][m]とおく。
・求めたい最小疲労度は、dp[N][1],dp[N][2],.....dp[N][M]の最も小さい疲労度となる。
→ dpを手書きで書いた(45分くらい...)

・書くとわかるが、dp表の対角線で切った左半分は無限大となる。
なぜなら、例えば都市3にDay1で辿り着くことは、本問題の場合不可能であるから。
よって、iの値によってmの範囲が固定される。

・また、初期条件としては、dp[0]=[0,0,0,0,..0]となる。ここは無限ではない。

・また、dp の無限大を 10**6 にすると、Codeはあってても1個もACされない。
→ 無限を入れたい場合は、10**10 とする癖をつけておくこと！！！

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
D = []
C = []

for i in range(N):
    D.append(int(input()))
for j in range(M):
    C.append(int(input()))

# dpは　行(N+1)×列(M+1) となる
dp = [[10**6]*(M+1) for i in range(N+1)]
for i in range(M+1):
    dp[0][i] = 0

for i in range(1,N+1):
    # Case1) dp[i][m] = dp[i][m-1] # 待機する場合
    # Case2) dp[i][m] = dp[i-1][m-1] + C[m-1]*D[i-1] # 進める場合
    for m in range(i,M+1):
        dp[i][m] = min(dp[i][m-1],dp[i-1][m-1]+C[m-1]*D[i-1])

#for i in range(N+1):
#    print(dp[i])
print(f"{min(dp[N])}")
