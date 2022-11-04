"""
BFS Maze: 壁あるやつ
Input
2 3
 1
0 1
 0 
1 0
 1
"""

while True:
    w, h = map(int,input().split())
    if w==0 and h==0:
        break
    A = []
    B = []

    for i in range(h):
        tmp = [0 for j in range(w-1)]
        A.append(tmp)

    for i in range(h-1):
        tmp = [0 for j in range(w)]
        B.append(tmp)

    for i in range(2*h-1):
        if i%2==0:
            ll = list(map(int,input().split()))
            for col in range(len(ll)):
                A[i//2][col]=ll[col]
        else:
            ll = list(map(int,input().split()))
            for col in range(len(ll)):
                B[i//2][col]=ll[col]

    visited = []
    for i in range(h):
        tmp = [-1 for j in range(w)]
        visited.append(tmp)

    visited[0][0]=1

    def bfs():
        que = [(0,0)]
        while len(que)!=0:
            v = que.pop(0)

            for d in [[-1,0],[1,0],[0,-1],[0,1]]:
                x = v[0]+d[0]
                y = v[1]+d[1]

                if not (0<=y<w) or not (0<=x<h):
                    continue

                if visited[x][y]!=-1:
                    continue

                if d==[-1,0]:
                    if B[v[0]-1][v[1]]==0:
                        que.append([x,y])
                if d==[1,0]:
                    if B[v[0]][v[1]]==0:
                        que.append([x,y])
                if d==[0,-1]:
                    if A[v[0]][v[1]-1]==0:
                        que.append([x,y])
                if d==[0,1]:
                    if A[v[0]][v[1]]==0:
                        que.append([x,y])

                visited[x][y] = visited[v[0]][v[1]]+1

    bfs()
    if visited[h-1][w-1]==-1:
        print(f"0")
    else:
        print(f"{visited[h-1][w-1]}")


"""
2 3
 1
0 1
 0
1 0
 1
9 4
 1 0 1 0 0 0 0 0
0 1 1 0 1 1 0 0 0
 1 0 1 1 0 0 0 0
0 0 0 0 0 0 0 1 1
 0 0 0 1 0 0 1 1
0 0 0 0 1 1 0 0 0
 0 0 0 0 0 0 1 0
12 5
 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0
 1 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 0 0 0 0
 0 0 1 0 0 1 0 1 0 0 0
0 0 0 1 1 0 1 1 0 1 1 0
 0 0 0 0 0 1 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 1 0 0
0 0
"""