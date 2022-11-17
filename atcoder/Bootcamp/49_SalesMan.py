"""
巡回セールスマン問題(Traveling Salesman: TSP)
理論を理解し、再帰DPでトライしたが、どうしても合わないので、
ボトムアップでやる。再帰DPも頭を冷やしてまたやる。

https://cnc-selfbuild.blogspot.com/2019/05/tsp-dp.html
集合はsetでもOKぽいが、intで2進数のbitでやるのがメインアプローチぽいので
それでやってみる

https://www.slideshare.net/hcpc_hokudai/advanced-dp-2016
https://qiita.com/kiura_369/items/d9e7853341a8405a898f

dp[S][v]:=頂点0からスタートして、
{0,1,2,3,...,n-1}の部分集合Sを巡回する|S|!通りの経路のうち最短のものの距離.
ただし、最後に頂点vに達した時のみを考える.

--Input--
4 6
0 1 2
1 2 3
1 3 9
2 0 1
2 3 6
3 2 4
--Output--
16
"""
import sys

V, E = map(int,input().split())
G = [[float('inf')]*V for i in range(V)]
for i in range(E):
    s,t,d = map(int,input().split())
    G[s][t] = d

dp = [[float('inf')]*V for i in range(1<<V)]
dp[0][0] = 0

for S in range(1<<V): # Sは集合をbitで表している
    for v in range(V): # vは配られる側の要素を表している
        for u in range(V): # uは配る側の要素を表している
            if not (S >> u) & 1 and S != 0:
                continue
            if (S >> v) & 1 == 0:
                if dp[S][u] + G[u][v] < dp[S|(1 << v)][v]: # | はOR演算子
                    dp[S | (1 << v)][v] = dp[S][u] + G[u][v] # 更新

if dp[(1<<V)-1][0] != float('inf'):
    print(dp[(1<<V)-1][0])
else:
    print(-1)
"""
import sys
sys.setrecursionlimit(20000)

# int bit, int v
def rec(bit, v):
    if dp[bit][v]!=-1:      # (A) 既に探索済みならメモ値を返す
        return dp[bit][v]

    if bit==0:
        if v==0:
            return 0
        else:
            return INF
    
    res=INF
    #prev_bit = bit & ~(1<<v) # bit{1,2,3}の時にv=1だとしたら、{2,3}としてprev_bitを決める
    
    for u in range(n):  #(C) 更新の条件
        if u==v: continue
        prev_bit = bit & ~(1<<u)
        if (not (prev_bit & (1<<u))):
            continue # uが集合に含まれてなければ
        
        print(f"***** u,bit,v = {u},{bit},{v} *****")
        res = min(res, rec(prev_bit,u)+dist[u][v])
    
    dp[bit][v]=res
    return res

# ---
n,m=map(int,input().split())
dist=[]
INF=float('inf')
for i in range(n):
    dist.append([0 for _ in range(n)])

for i in range(m):
    sid,eid,d=map(int,input().split())
    dist[sid][eid]=d

dp=[]
for i in range((1<<6)+1): # dpテーブルは余裕をもったサイズにする
    dp.append([-1 for _ in range(20)])

ans = rec((1<<n)-1,0)
print(ans)

for i in range(4):
    print(*dist[i])
"""