"""
Ice Walk
方針:
・深さ優先する
・

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

def dfs(x,y):
    global cnt
    if x <0 or x>=h or y <0 or y>=w:
        return

    if visited[x][y] != -1:
        return
    
    visited[x][y]=9
    
    if A[x][y] != 1:
        return

    cnt+=1
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    ll.append(cnt)
    cnt = 0

max_cnt = 0
for yy in range(w):
    for xx in range(h):
        visited = []
        ll =[]
        cnt = 0
        for i in range(h):
            tmp = []
            for j in range(w):
                tmp.append(-1)
            visited.append(tmp)
        
        dfs(xx,yy)
        if len(ll)!=0:
            ll_max = max(ll)
        else:
            ll_max = 0
        max_cnt = max(max_cnt,ll_max)

print(max_cnt)
