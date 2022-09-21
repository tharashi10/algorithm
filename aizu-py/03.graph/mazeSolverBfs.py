"""
MazeをBfs(幅優先探索)で解く
注意; sx,sy共に1<=sx,sy<=R,X を満たすような座標系とみなす。
原点は左上。
入力
7 8  # 行数R/ 列数C
2 2  # Start sy,sx
4 5  # Goal  gy,gx
########
#......#
#.######
#..#...#
#..##..#
##.....#
########
---
出力
11 最小ステップ数
"""
from collections import deque

def bfs(maze, sx, sy, gx, gy, visited):
    queue = deque([[sy,sx]]) #[2, 2]始点
    visited[sy][sx] = 0

    while queue:
        y, x = queue.popleft()

        if [y,x] == [gy,gx]:
            return visited[y][x]

        print(y,x)
        for h,l in ([[0,-1],[0,1],[-1,0],[1,0]]):
            Y, X = y+h, x+l
            if visited[Y][X] == None and maze[Y][X] == ".":
                visited[Y][X] = visited[y][x] +1
                queue.append([Y, X])

if __name__ == "__main__":
    R, C = map(int,input().split())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())
    visitedList = [[None]*C for _ in range(R)]
    maze = [input() for i in range(R)]

    sx, sy, gx, gy = sx-1, sy-1, gx-1, gy-1 # 0-originに書き戻す
    print(bfs(maze, sx, sy, gx, gy, visitedList))
    print(visitedList)
