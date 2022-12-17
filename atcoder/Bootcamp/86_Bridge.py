"""
Union-Find
https://www.youtube.com/watch?v=oLO7kLNJt7A

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
        self.parent = [i for i in range(n)]
    
    def find(self,x):
        if self.parent[x]==x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        self.parent[x] = y
    
    def same(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        return rx == ry

def main():
    V,E = map(int,input().split())
    
    pair = []
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
        
        if uf.same(o1,o2):
            print(f"No ***** parent={uf.parent}")
        else:
            print(f"Yes: o1={o1}, o2={o2} ***** parent={uf.parent}")


if __name__=="__main__":
    main()
