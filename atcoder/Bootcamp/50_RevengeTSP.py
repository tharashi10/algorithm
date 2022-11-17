#V, E = map(int,input().split())
#G = [[float('inf')]*V for i in range(V)] # 存在しないパスはinfになるように、最初にすべてinfにしておく
for i in range(E):
    s,t,d = map(int,input().split())
    G[s][t] = d # s,tは0以上V-1以下なので、デクリメントの必要はない
dp = [[float('inf')]*V for i in range(2**V)] # dpの長さは2^V必要
dp[0][0] = 0 # 0から出発するのでdp[0][0]を0にしておく


for S in range(2**V): # Sは集合をbitで表している
    for v in range(V): # vは配られる側の要素を表している
        for u in range(V): # uは配る側の要素を表している
            if not (S >> u) & 1 and S != 0: # ①
                continue
            if (S >> v) & 1 == 0: # ②
                if dp[S][u] + G[u][v] < dp[S | (1 << v)][v]:
                    dp[S | (1 << v)][v] = dp[S][u] + G[u][v] # ③

# 全ての要素が含まれていて、末項が0のものの最小コストを出力する
# infだった場合は到達できないということなので-1を出力する
if dp[2**V-1][0] != float('inf'):
    print(dp[2**V-1][0])
else:
    print(-1)