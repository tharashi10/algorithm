"""
Union Find
・良問だそう
・ナイーブな感じで解くとTLEする(コメントアウト)
・86番のようにEdgeを除外していくのではなく、Edgeを追加して考える。
そうすると、非連結だったGraphがEdge追加により、新たに連結される。
例えば Node {Ai},{Bi}が連結されると、「既にAiと連結されているNode」と
「既にBiと連結されているNode」が連結されるので、掛け算した分だけ非連結なペアが減る。

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
import sys
sys.setrecursionlimit(int(1e7))
class UnionFind:
    def __init__(self,n):
        self.n = n
        self.parent = [-1]*n    #Root
        self.rank = [0]*n       #深さ
        self.size = [1]*n       #既に連結されているNodeの数(Groupのメンバ)
    
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
        
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
            self.size[ry] += self.size[rx]
        else:
            self.parent[ry] = rx
            self.size[rx] += self.size[ry]
            if self.rank[rx] == self.rank[ry]:
                self.rank[ry] += 1

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
    
    ans = [0]*M
    ans[0] = int(N*(N-1)/2)

    pair = list(reversed(pair))
    uf = UnionFind(N)
    for i in range(M-1):
        a,b = pair[i]
        if uf.find(a)==uf.find(b):
            ans[i+1] = ans[i]
        else:
            ans[i+1] = ans[i] - uf.size[uf.find(a)] * uf.size[uf.find(b)]
        uf.union(a,b)
    
    ## Parent : IDの小さい方がRootになる
    ## Rank   : Parent配列に沿う
    ## Size   : IDの小さい方にグループサイズを委ねる
   
    for x in reversed(ans):
        print(x)
    
if __name__=="__main__":
    main()




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
"""