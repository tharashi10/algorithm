"""
Ice Walk
方針:
・深さ優先する
・

Output
3
3
1 1 0
1 0 1
1 1 0
Input
5
"""
w = int(input())
h = int(input())

A = []
for i in range(h):
    A.append(list(map(int,input().split())))

def dfs(x,y):
    if x <0 p x>=w or y <0 or y>=h:
        return
    
