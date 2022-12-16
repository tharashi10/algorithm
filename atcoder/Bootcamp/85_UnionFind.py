"""
Union Find
このスライドが最もわかりやすい
https://atcoder.jp/contests/atc001/tasks/unionfind_a

set.recutsionlimit()を入れないと、
テストケース21.でRuntime Errorになる。(結構な数をテストケースに入れてある模様)
---
5 12
0 1 4
0 2 3
1 1 2
1 3 4
1 1 4
1 3 2
0 1 3
1 2 4
1 3 0
0 0 4
1 0 2
1 3 0
---
0
0
1
1
1
0
1
1
"""
import sys
sys.setrecursionlimit(int(1e7))

def main():
    N,M = map(int,input().split())
    par = [i for i in range(N)]
    
    def root(x): # 自分の親を見つける
        if par[x]==x:
            return x
        else:
            par[x]=root(par[x]) # 経路圧縮
            return par[x]
    
    def same(x,y): # 親が一緒か判定する
        rx = root(x)
        ry = root(y)
        return rx == ry

    def unite(x,y): # それぞれの親を確認して、異なるなら親をマージする
        rx = root(x)
        ry = root(y)
        if rx==ry:
            return None
        par[rx]=ry
    
    query = []

    for _ in range(M):
        query.append(list(map(int,input().split())))
    
    for i in range(M):
        q = query[i][0]
        x = query[i][1]
        y = query[i][2]
        if q==0:
            unite(x,y)
            continue
        elif q==1:
            if same(x,y):
                print('1')
            else:
                print('0')

if __name__=="__main__":
    main()
