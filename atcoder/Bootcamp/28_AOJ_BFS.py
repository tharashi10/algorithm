"""
BFS
方針: BFS(x)で値を探索しにいく
https://qiita.com/drken/items/996d80bcae64649a6580
ポイント:
・いつ距離distを入れるか
・発見済みのものはAppendしない(ここ、と書いたとこ)

4
1 2 2 4
2 1 4
3 0
4 1 3
---
1 0
2 1
3 2
4 1
"""
n = int(input())
A = [[]]
dist = [0,0]+[-1 for _ in range(n-1)]
que = [1]

for i in range(n):
    tmp = list(map(int,input().split()))
    k = tmp[1]
    ll = [tmp[j+2] for j in range(k)]
    A.append(ll)

def bfs(x):
    while len(que)!=0:
        vid = que.pop(0)
        if vid==x:
            break
        for v in A[vid]:
            if dist[v]!=-1: #←ここ
                continue
            dist[v]=(dist[vid]+1)
            que.append(v)

bfs(100) #　100は適当な値
for i in range(1,n+1):
    print(f"{i} {dist[i]}")