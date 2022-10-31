""":
How many islands?
方針
・再帰関数版の深さ優先探索で実装してみる
・Inputがやや癖があるので、各々のケースに対してDFSを適用させる

https://atcoder.jp/contests/atc001/tasks/dfs_a
Input
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
Output
9
"""

A = []
h,w = map(int,input().split())
Already = [[-1]*w]*h
time = 0

for i in range(h):
    A.append(list(map(int,input().split())))

def dfs(xid,yid):
    global time
    if xid<0 or xid>h or yid<0 or yid>=w:
        return
    
    if A[xid][yid]==0:
        #print("0000")
        return 
    
    if Already[xid][yid] != -1:
        return

    Already[xid][yid] = time
    time+=1

    dfs(xid+1,yid  )
    dfs(xid-1,yid  )
    dfs(xid  ,yid+1)
    dfs(xid  ,yid-1)

dfs(0,0)
print(Already)