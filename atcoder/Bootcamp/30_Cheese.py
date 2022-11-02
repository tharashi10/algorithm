"""
自力で行けた。しかもE問題(初)
Cheese:
「最短時間を求める」と問題文にある
4 5 2
.X..1
....X
.XX.S
.2.X.
----
12
"""

h,w,n = map(int,input().split())
A = []
sx,sy = -1,-1
for i in range(h):
    st = input()
    tmp = []
    for j in range(w):
        if st[j]=='S':
            sx,sy = i,j
        tmp.append(st[j])
    A.append(tmp)

def bfs(s_x,s_y,goal_num):
    while len(que)!=0:
        v = que.pop(0)
        if A[v[0]][v[1]] == str(goal_num):
            tmp = [v[0],v[1]]
            return tmp,dist[v[0]][v[1]]
        
        if v[0]<0 or v[0]>=h or v[1]<0 or v[1]>=w:
            break
        if A[v[0]][v[1]] =='X':
            break
        for m in [[-1,0],[1,0],[0,-1],[0,1]]:
            xx = v[0]+m[0]
            yy = v[1]+m[1]
            if xx<0 or xx>=h or yy<0 or yy>=w:
                continue
            if A[xx][yy] =='X':
                continue
            if dist[xx][yy]!=-1:
                continue
            que.append([xx,yy])
            dist[xx][yy] = dist[v[0]][v[1]]+1
           
ans = 0
for num in range(1,n+1): #ここを0始まりとすると、startできなくなるから注意(Start=Goalになる)
    que = [(sx,sy)]
    dist = []

    for i in range(h):
        dist.append([-1 for _ in range(w)])
    dist[sx][sy] = 0
    #print(f"unpack: sx,sy,num: {sx},{sy},{num}")
    start,cnt = bfs(sx,sy,num)
    sx,sy = start[0], start[1]
    ans+=cnt

print(f"{ans}")
