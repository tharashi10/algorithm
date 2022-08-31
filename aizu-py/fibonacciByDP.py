"""Dynamic Programming
動的計画法=「漸化式」+「解の保存」
(別名:メモ化再帰)
何がDynamicか:[動的配列にメモを保存しつつ処理すること]
a_n= a_n-1 + a_n-2
※ returnの後ろは実行されない
"""
import time

#メモリスト用意
MAX = int(101)
dp = [-1 for _ in range(MAX)]

def fibonacci(n :int) -> int:
    if n<=1 :
        dp[n] = n
        return n
    else:
        if dp[n]==-1:
            x = fibonacci(n-1)
            y = fibonacci(n-2)
            dp[n] = (fibonacci(n-1) + fibonacci(n-2))
        else:
            return dp[n]

start = time.time()
print(fibonacci(99))
print(dp)
end = time.time()
print(end-start)
## n=99とかだと、メモ化なしの再帰だと全然返ってこない(だいぶ遅い)