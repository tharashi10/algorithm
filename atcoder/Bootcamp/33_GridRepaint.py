"""
・自力で行けた。15分でACできた
方針:
・最短経路を求めて、経路以外で黒にしてもOKな箇所がスコアになるはず
・つまり、Score=(H*W)-(Blackのマス)-(最短ステップ数)

--Input--
3 3
..#
#..
...
--Score--
2
"""
h,w = map(int,input().split())
A = []
for _ in range(h):
    st = input()
    A.append([st[i]for i in range(w)])

visited = []
for i in range(h):
    visited.append([-1 for _ in range(w)])

visited[0][0] = 1
def bfs():
    que = [[0,0]]
    while len(que)!=0:
        v = que.pop(0)
        if v == [h-1,w-1]:
            break
        for d in [(-1,0),(1,0),(0,1),(0,-1)]:
            x = v[0]+d[0]
            y = v[1]+d[1]

            if not (0<=x<h) or not (0<=y<w):
                continue
            if A[x][y] == '#':
                continue
            if visited[x][y]!=-1:
                continue
            visited[x][y]=visited[v[0]][v[1]]+1
            que.append([x,y])
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if A[i][j]=='#':
                cnt+=1
    
    #print(f"cnt(#):{cnt} and cnt(.):{h*w-cnt}")
    #print(f"visited[h-1][w-1]:{visited[h-1][w-1]}")
    if visited[h-1][w-1]==-1:
        return -1
    else:
        return h*w-(cnt+visited[h-1][w-1])

print(bfs())
