""":
Depth First Search(深さ優先探索)
方針
・DFSには「Stackを利用した解き方」と「再帰を利用した解き方」の2種類がある
・流れ
1.既に探索済みかをCheckする
2.もし初めて見たのであれば、初めて見たメモd[now]を更新
3.隣接する頂点についてDFS(neighbor)を実施
4.調べ終えたら調べ終わったタイミングリストf[now]を更新
・DFSの行きがけ、帰りがけのメモを使う書き方を忘れてしまっていたので、
シンプルな対称グラフでJupyterで確認してみた

Input--
4
1 1 2
2 1 4
3 0
4 1 3
Output--
1 1 8
2 2 7
3 4 5
4 3 6
"""
time =1
n = int(input())
v = [0]
A = [-1]*(n+1) #行きがけのメモ
B = [-1]*(n+1) #帰りがけのメモ

for i in range(n):
    vv = list(map(int, input().split()))
    v.append(vv[2:]) #隣接リスト作成

def dfs(now):
    global time
    if A[now] != -1:
        return
    A[now] = time
    time+=1
    
    for i in range(len(v[now])):
        dfs(v[now][i])
    B[now] = time
    time+=1

for k in range(1,n+1): # 隣接を持たないノードを回避するためにLoopする
    dfs(k)
    print(f"{k} {A[k]} {B[k]}")
