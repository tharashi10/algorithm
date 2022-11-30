"""
本選会場
黙ってPrim法で解いてみる.
→K個の会場として、切りたいが、答えが合わないので、
クラスカル法に切り替える
→クラスカル実装で出てくるUnion-Findはこちら
(https://atcoder.jp/contests/atc001/tasks/unionfind_a)

4 3 1
1 2 2
2 3 9
2 4 5
16

5 6 2
1 2 5
1 3 3
2 3 4
2 5 7
3 4 6
4 5 5
12
"""

def main():
    # Union-FIndを使って、頂点間の連結判定をする
    def root(x):
        if x==par[x]:
            return x
        par[x] = root(par[x])
        return par[x]
    
    def unite(x,y):
        rx = root(x)
        ry = root(y)
        if rx==ry:
            return None
        if rx<ry:
            par[rx]=ry
        else:
            par[ry]=rx
    
    def same(x,y):
        rx = root(x)
        ry = root(y)
        return rx==ry

    V,E,K = map(int,input().split())
    G = []
    for i in range(E):
        s,t,c = map(int,input().split())
        G.append((c,s,t))

    par = [i for i in range(V+1)]
    G.sort()
    ans = 0
    edge_cnt = 0
    for c,u,v in G:
        edge_cnt+=1
        if not same(u,v):
            unite(u,v)
            ans+=c
            if edge_cnt>=V-K:
                break
    
    print(ans)


if __name__=="__main__":
    main()


"""Prim
import heapq

def main():
    V,E,K = map(int,input().split())
    G = [[] for _ in range(V+1)]
    for i in range(E):
        s,t,c = map(int,input().split())
        G[s].append((t,c))
        G[t].append((s,c))
    
    print(G)

    used = [0]*(V+1)
    used[1] = 1
    que = [(c,u) for u,c in G[1]]
    heapq.heapify(que)

    ans=0
    cnt=0
    while que:
        cv,v = heapq.heappop(que)
        if used[v]:
            continue
        used[v]=1
        ans+=cv
        cnt+=1
        if cnt==V-K:
            break
        for k,c in G[v]:
            if used[k]:
                continue
            heapq.heappush(que,(c,k))
    
    print(ans,cnt)

if __name__=="__main__":
    main()

"""