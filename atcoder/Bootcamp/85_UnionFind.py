"""
Union Find
このスライドが最もわかりやすい
https://atcoder.jp/contests/atc001/tasks/unionfind_a
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

def main():
    N,M = map(int,input().split())
    par = [i for i in range(N)]
    
    def find(x): # 自分の親を見つける
        if par[x]==x:
            return x
        else:
            par[x]=find(par[x]) # 経路圧縮
            return par[x]
    
    def same(x,y): # 親が一緒か判定する
        return find(x)==find(y)

    def unite(x,y): # それぞれの親を確認して、異なるなら親をマージする
        x = find(x)
        y = find(y)
        if x==y:
            return 0
        par[x]=y
    
    for _ in range(M):
        c,x,y = map(int,input().split())
        if c==0:
            unite(x,y)
            continue
        elif c==1:
            if same(x,y):
                print("1")
            else:
                print("0")

if __name__=="__main__":
    main()
