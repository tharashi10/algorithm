"""
<ALDS1_10_B>
簡単だろうなと思っていたけど、
ちゃんと考えると普通にNotEasy.(D/E問題だと思う)
漸化式
--------
連鎖行列積
Input
6
30 35
35 15
15 5
5 10
10 20
20 25
------
Output
15125
"""

def calc():
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            # i と j が定まる
            j = i + l - 1
            m[i][j] = 2**20
            #print(m)
            for k in range(i, j):
                # dp[i][j] パート
                # Ex. M1 M2 M3 M4 M5
                # dp[1][5] = (M1M2M3)のコスト + (M4M5)のコスト
                #           + M1の行数 × M3の列数 × M5の列数  
                m[i][j] = min(m[i][j], m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j])

if __name__ == "__main__":
    n = int(input())
    p = [0]*(n+1)
    for i in range(n):
        # 途中の列については、スカラー演算時に相殺されるため上書きしちゃう
        p[i], p[i+1] = map(int, input().split())
    # N行N列の正方行列を用意する(これが動的計画法の最小Costをメモる行列となる)
    m = [[0]*(n+1) for _ in range(n+1)]
    calc()
    print(m[1][n])
