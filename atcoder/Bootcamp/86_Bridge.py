"""
Union-Find
https://www.youtube.com/watch?v=oLO7kLNJt7A
ACできた

ポイントは、Edge(辺)を外してみた時に、残っているノード/エッジでUnionFindして、
親が一つになれば、そのEdgeは「橋じゃない」。
→ なぜなら、任意の2つのノードが到達可能になるため。
→　例のケースのように閉路がありその中の一つのEdgeを取り除いた場合は、箸にならない。

もし、着目しているEdgeを取り除いてみて、親が2つ以上になれば、
任意の2つのノードは辿り着かないことが言えるので、その着目Edgeは橋であるといえる。

7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7
--
4
"""
import sys
sys.setrecursionlimit(int(1e7))

class UnionFind:
    def __init__(self,n):
        self.n = n
        self.parent = [-1]*n
    
    def find(self,x):
        if self.parent[x]==-1: # 自分自身が根である場合
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        self.parent[rx] = ry
    
    def same(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        return rx == ry

def main():
    V,E = map(int,input().split())
    
    pair = []
    cnt = 0
    for _ in range(E):
        a,b = map(int,input().split())
        a-=1
        b-=1
        pair.append((a,b))
    for i in range(E):
        uf = UnionFind(V)
        for j in range(E):
            if i==j:
                continue
            u,v = pair[j]

            uf.union(u,v)
        o1,o2 = pair[i]
            
        if not uf.same(o1,o2):
            cnt+=1
    
    print(cnt)        


if __name__=="__main__":
    main()
