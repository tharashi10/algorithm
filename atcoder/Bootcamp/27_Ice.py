"""
Ice Walk
方針:
・普通に苦戦した
・重要なポイント: 「ここ」と書いた部分
頭では異なるパスではVisitedを初期化すべきとわかってたけど、
実装ができなかった。パスが終わるのは、4方向のdfs()が全部完了した後になる。

・重要なポイント: dfsでは基本に習って引数には位置だけを設定したかった。
けど、おそらくそれだと最終的に問題25のような島のサイズを出すことになっちゃうので、
位置だけでなく、pointも引数に入れるようにした。

DFSの型はわかった。
DFS問題は、現時点では時間かかると思うけど、もう少しDFSの問題を練習する(やるなら多分EOP)

Input
3
3
1 1 0
1 0 1
1 1 0
Output
5

Input(2)
5
3
1 1 1 0 1
1 1 0 0 0
1 0 0 0 1
Output(2)
5

"""

import sys
sys.setrecursionlimit(10**8)
w = int(input())
h = int(input())

A = []
for i in range(h):
    A.append(list(map(int,input().split())))

cnt = 0
def dfs(x,y,pts):
    global cnt
    
    if cnt < pts:
        cnt = pts
    
    if x <0 or x>=h or y <0 or y>=w:
        return
    
    if A[x][y] != 1:
        return
    
    A[x][y]=0   #←ここ
    dfs(x+1,y,pts+1)
    dfs(x-1,y,pts+1)
    dfs(x,y-1,pts+1)
    dfs(x,y+1,pts+1)
    A[x][y]=1   #←ここ
    #print(f"pts: {pts}")

for i in range(w):
    for j in range(h):
        dfs(i,j,0)

print(cnt)
