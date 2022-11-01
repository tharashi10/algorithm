"""
Rooted Tree:
方針:
・深さ優先(位置を引数に)で解く←当たり前
・[Point]累積和で計算するべし(各操作では根のノードだけに値を入れておく)
・AterContestTestCaseが通らないため、リストAを双方向にして、なおかつ
一度訪れたやつは再度計算しないよチェックを入れればいけるはず

・(imos法でも解ける模様)

Input
4 3
1 2
2 3
2 4
2 10
1 100
3 1
Output
100 110 111 110

After contest Case
4 3
1 4
1 3
2 3
2 10
1 100
3 1
--
100 111 101 100
"""

import sys
sys.setrecursionlimit(10**7)

n,m = map(int,input().split())
A = [[] for i in range(n)]
values = [0 for i in range(n)]

for i in range(n-1):
    fro,to = map(int,input().split())
    fro,to = fro-1, to-1
    A[fro].append(to)
    A[to].append(fro)

for j in range(m):
    pid, pts = map(int,input().split())
    values[pid-1]+=pts

def dfs(vid, prev=-1):
    for nxt in A[vid]:
        if nxt == prev:
            continue
        values[nxt]+= values[vid] 
        dfs(nxt,vid)  

dfs(0) 
print(*values)