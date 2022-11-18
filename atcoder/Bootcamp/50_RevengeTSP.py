"""
無向グラフの巡回セールスマン問題
Revenge of Traveling Salesman Problem
Input
3 3
1 2 1 6
2 3 2 6
3 1 3 6
--コストとパターン数を出す
6 2
"""

V,E = map(int,input().split())
G  = []
GT = []
for i in range(V):
    G.append([0 for _ in range(V)])
    GT.append([0 for _ in range(V)])

for i in range(E):
    s,t,d,time=map(int,input().split())
    G[s-1][t-1]=d
    G[t-1][s-1]=d
    GT[s-1][t-1]=time

#dp = []
#for j in range(1<<V):
#    dp.append([float('inf') for i in range(V)])
dp = [[float('inf')]*V for i in range(1<<V)]
dp[0][0] = 0

for S in range(1<<V):
    for v in range(V):
        for u in range(V):
            if not (S>>u) &1 and S !=0:
                continue
            
            if (S>>v) & 1==0: # Sにはvが含まれない元で
                if dp[S][u]+G[u][v] < dp[S|(1<<v)][v]: #動かなかったらここを見直せ
                    dp[S|(1<<v)][v]=dp[S][u]+G[u][v]

if dp[(1<<V)-1][0] != float('inf'):
    print(dp[(1<<V)-1][0])




"""
def tsp(N, M, G, start=0):
    dp = [[float("inf")] * N for _ in range(1 << N)]
    dp[0][start] = 0
    ep = [[0] * N for _ in range(1 << N)]
    ep[0][start] = 1
    for V in range(1 << N):
        for u in range(N):
            for v, w, t in G[u]:
                if (V >> v) & 1 == 0 and dp[V][u] + w <= t:
                    if dp[V][u] + w < dp[V | (1 << v)][v]:
                        dp[V | (1 << v)][v] = dp[V][u] + w
                        ep[V | (1 << v)][v] = ep[V][u]
                    elif dp[V][u] + w == dp[V | (1 << v)][v]:
                        ep[V | (1 << v)][v] += ep[V][u]

    ans1 = dp[(1 << N) - 1][start]
    if ans1 == float("inf"):
        ans1 = -1
    ans2 = ep[(1 << N) - 1][start]

    return ans1, ans2


def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v, w, t = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append((v, w, t))
        G[v].append((u, w, t))

    ans1, ans2 = tsp(N, M, G)
    if ans1 == -1:
        print("IMPOSSIBLE")
    else:
        print(ans1, ans2)


if __name__ == "__main__":
    main()
"""