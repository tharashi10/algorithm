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
    B = []
    for _ in range(V):
        A.append(list(map(int,input().split())))
    
    B = [[s[1],s[0]] for s in A]

    A.sort()
    B.sort()

    G = [[] for _ in range(V)]
    for i in range(V-1):
        rx,ry = A[i][0], A[i][1]
        tx,ty = A[i+1][0], A[i+1][1]
        mn = min(abs(rx-tx),abs(ry-ty))
        G[i].append((i+1,mn))
        G[i+1].append((i,mn))

        sx,sy = B[i][1], B[i][0]
        lx,ly = B[i+1][1], B[i+1][0]
        mn_y = min(abs(sx-lx),abs(sy-ly))
        G[i].append((i+1,mn_y))
        G[i+1].append((i,mn_y))
    
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
