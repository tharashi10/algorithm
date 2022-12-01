"""
方針
・遠目の2点は結ばれない
・X座標でソートして、隣り合う座標同士のコストを考えていく
→これでエッジの数を減らすことができる
https://emtubasa.hateblo.jp/entry/2018/12/02/000000_1

3
1 5
3 9
7 8
"""
import heapq

def main():
    V = int(input())
    A = []
    for ids in range(V):
        A.append(list(map(int,input().split()))+[ids]) # [1,5,0] : x,y,ids
    
    A.sort(key=lambda x:x[0])

    G = [[] for _ in range(V)]
    # xをソートする
    for i in range(V-1):
        rx,ry = A[i][0], A[i][1]
        tx,ty = A[i+1][0], A[i+1][1]
        mn = min(abs(rx-tx),abs(ry-ty))
        ids = A[i][2]
        ids_ = A[i+1][2]
        G[ids].append((ids_,mn))
        G[ids_].append((ids,mn))
    
    A.sort(key=lambda x:x[1])
    # yをソートする
    for j in range(V-1):
        sx,sy = A[j][0], A[j][1]
        lx,ly = A[j+1][0], A[j+1][1]
        mn_y = min(abs(sx-lx),abs(sy-ly))
        ids = A[j][2]
        ids_ = A[j+1][2]
        G[ids].append((ids_,mn_y))
        G[ids_].append((ids,mn_y))

    que = [(c,w) for w,c in G[0]]
    heapq.heapify(que)

    used=[0]*V
    used[0]=1

    ans = 0
    while que:
        cv,v = heapq.heappop(que)
        if used[v]:
            continue
        used[v]=1
        ans+=cv
        for u,cu in G[v]:
            if used[u]:
                continue
            heapq.heappush(que,(cu,u))
    
    print(ans)

if __name__=="__main__":
    main()
