"""
Union Find
ナイーブな感じで解くとTLEする(コメントアウトした)

4 5
1 2
3 4
1 3
2 3
1 4
--
0
0
4
5
6
"""
from itertools import combinations
class UnionFind:
    def __init__(self,n):
        self.n = n
        self.parent = [-1]*n
    
    def find(self,x):
        if self.parent[x] == -1:
            return x
        else:
            self.parent[x] =  self.find(self.parent[x])
            return self.parent[x]

    def union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        if rx==ry:
            return
        self.parent[rx] = ry

    def same(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        return rx ==ry

def main():
    N,M = map(int,input().split())
    pair = []
    for _ in range(M):
        a,b = map(int,input().split())
        a-=1
        b-=1
        pair.append((a,b))
    
    for i in range(M):
        uf = UnionFind(N)
        for j in range(M):
            if j<=i:
                continue
            a,b = pair[j]
            uf.union(a,b)
        v1,v2 = pair[i]
        l = list(combinations([i for i in range(N)],2))
        
        cnt = 0 # 根が同じであるノードをCount
        for i in range(len(l)):
            u1,u2 = l[i]
            if uf.same(u1,u2):
                cnt +=1
        print(len(l)-cnt)
        
if __name__=="__main__":
    main()
