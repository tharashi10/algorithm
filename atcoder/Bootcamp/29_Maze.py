"""
方針: 28と同じ。手数を決めたらステップ数をFIXさせる

Input---
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########
Output---
12
"""
h,w = map(int,input().split())
s_x, s_y = map(int,input().split())
g_x, g_y = map(int,input().split())

A = []
for i in range(h):
    st = input()
    A.append([st[j]for j in range(w)])

dist = []
for _ in range(h):
    tmp = []
    for _ in range(w):
        tmp.append(-1)
    dist.append(tmp)

que = [[s_x-1,s_y-1]]
dist[s_x-1][s_y-1] = 0
print(f"s_x-1,s_y-1 : {s_x-1,s_y-1}")
print(A)
def bfs():
    while len(que)!=0:
        v = que.pop(0)
        if v[0]<0 or v[0]>=h or v[1]<0 or v[1]>=w:
            break
        print(f"v[0],v[1]:{v[0],v[1]}")
        if A[v[0]][v[1]]=='#':
            break

        for l in [[0,1],[0,-1],[1,0],[-1,0]]:
            x = v[0]+l[0]
            y = v[1]+l[1]
            if x<0 or x>=h or y<0 or y>=w:
                continue
            if A[x][y]=='#':
                continue
            if dist[x][y]!=-1:
                continue
            
            dist[x][y] = dist[v[0]][v[1]]+1
            que.append([x,y])
bfs()
print(f"dist : {dist}")
