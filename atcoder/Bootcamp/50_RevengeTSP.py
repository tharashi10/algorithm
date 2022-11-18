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

--G: 3行
[[1, 1, 6], [2, 3, 6]] #ノード0と繋がる奴ら
[[0, 1, 6], [2, 2, 6]] #ノード1と繋がる奴ら
[[1, 2, 6], [0, 3, 6]] #ノード2と繋がる奴ら

--dp
0   inf inf
inf inf inf
inf 1   inf
2   inf inf
inf inf 3
6   inf inf
inf 5   3
6   inf 5

--ep
1 0 0
0 0 0
0 1 0
1 0 0
0 0 1
1 0 0
0 1 1
2 0 1

[大まかな流れ]
1. Graph用の表Gを作る
2. 表DPを作る/表EPを作る(経路用)
3. 初期値を設定する
4. 更新のFor文を書く
5. 求めたいdp[(1<<V)-1][0]を標準出力する

普通にTLEするので、if "__name__"=="main":の記述にする
→ 1000msくらいの差が出る模様

"""

def main():
    V,E = map(int,input().split())
    G = [[] for _ in range(V)]

    for i in range(E):
        s,t,d,time = map(int,input().split())
        s-=1
        t-=1
        G[s].append([t,d,time])
        G[t].append([s,d,time])


    start = 0
    dp = [[float('inf')]*V for _ in range(1<<V)]
    ep = [[0] * V for _ in range(1 << V)]
    dp[0][start]=0
    ep[0][start]=1
    for S in range(1<<V):
        for k in range(V):
            for v, d, t in G[k]: #ノードkと繋がっているノードたちに対して
                #print(v, d, t)
                if (S>>v) &1==0 and dp[S][k] + d<=t : # ノードkが始点で、次のノードvに遷移できる場合
                    if dp[S][k] + d <dp[S|(1<<v)][v]: # ノードvに遷移できる場合
                        dp[S|(1<<v)][v] = dp[S][k] + d # 更新
                        ep[S|(1<<v)][v] = ep[S][k]     # 更新
                    elif dp[S][k] + d == dp[S|(1<<v)][v]: # dpが等しい場合
                        ep[S|(1<<v)][v] += ep[S][k]     # epのみ更新

    ans1 = dp[(1 << V) - 1][start]
    ans2 = ep[(1 << V) - 1][start]
    if ans1 == float("inf"):
        print("IMPOSSIBLE")
    else:
        print(ans1, ans2)

if __name__ == "__main__":
    main()



#print(f"********")
#for i in range(1<<V):
#    print(*ep[i])


"""
https://atcoder.jp/contests/s8pc-1/submissions/35018509
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