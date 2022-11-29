"""
全点対間最短経路 = 任意の2頂点間の最短距離を求める問題
ワーシャルフロイド法で
→ほぼほぼ自力で行けた
注意: INF=10**10で置き換えると計算しちゃうので、
INF=float('inf')で計算すること

4 6
0 1 1
0 2 5
1 2 2
1 3 4
2 3 1
3 2 7
---
0 1 3 4
INF 0 2 3
INF INF 0 1
INF INF 7 0
"""

INF = float('inf')

def main():
    V,E = map(int,input().split())

    dp = [[INF]*V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            if i==j:
                dp[i][j]=0
    
    for _ in range(E):
        s,t,w = map(int,input().split())
        dp[s][t] = w
    
    # Warshall part
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])
    
    if not is_negative(dp):
        for i in range(V):
            for j in range(V):
                if dp[i][j]==INF:
                    dp[i][j]="INF"
        [print(*dp[i]) for i in range(V)]
    else:
        print(f"NEGATIVE CYCLE")

def is_negative(dp):
    for i in range(len(dp)):
        if dp[i][i] < 0:
            return True
    return False
    
if __name__ == "__main__":
    main()
