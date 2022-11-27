"""
船旅
ダイクストラで解く
途中でより短い経路が増えていく問題
方針
・入力に従い、隣接グラフを更新する
・最短経路は、ダイクストラで求める

→56番の型はチラ見したが、TLEせずほぼ自力で行けた
ポイントは3つ
1) 隣接行列を作る: ノード間がつながっているか表現する
2) ノード間距離のリスト : 各ノード間の距離を表現する
3) 移動過程の累積距離リスト : スタート地点ごとの最短の累積距離を表現する
で、これら三つをダイクストラメソッドに放り込む

input--
3 8
1 3 1 10
0 2 3
1 2 3 20
1 1 2 5
0 3 2
1 1 3 7
1 2 1 9
0 2 3
output--
-1
15
12
"""

import heapq

def main():
    INF = 10**10
    V,k = map(int,input().split())
    G = [[] for _ in range(V+1)]
    dic = {}

    for _ in range(k):
        ll = list(map(int, input().split()))
        if len(ll)==3:
            start = ll[1]
            goal = ll[2]
            sum_dist = [INF]*(V+1)
            sum_dist[start]=0
            ans = dijkstra(start, G, sum_dist, dic)
            if ans[goal] != INF:
                print(ans[goal])
            else:
                print(f"-1")
        else:
            s,t,d = ll[1],ll[2],ll[3]
            if (dic.get((s,t)) is None):
                G[s].append(t)
                G[t].append(s)
                dic[(s,t)] = d
                dic[(t,s)] = d
            elif (dic.get((s,t)) is not None and (dic[(s,t)] > d)):
                dic[(s,t)] = d
                dic[(t,s)] = d
                

def dijkstra(s,G,sum_dist,dic):
    hq = [(0,s)] # (Weight, Node)
    while hq:
        cost, now = heapq.heappop(hq)
        for next in G[now]: # G= [[1,2],[3],[1,2]]
            tmp = cost + dic[(now,next)] # 今現時点でのコスト＋次のステップで増えるコスト
            if tmp < sum_dist[next]:
                sum_dist[next] = tmp
                heapq.heappush(hq,(tmp,next)) # 更新済みのコストと次ノードをヒープへ
    return sum_dist

if __name__ == "__main__":
    main()
