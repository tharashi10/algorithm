""":
How many islands?
わかった
→ アルゴリズムノート(2)のP4に図を記載

方針
・再帰関数版の深さ優先探索で実装する
・Inputがやや癖があるので、各々のケースに対してDFSを適用させる
・一回到達した陸は、重複しないように海にしちゃう

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
reached = [[False]*w]*h
cnt = 0

for i in range(h):
    A.append(list(map(int,input().split())))

def dfs(xid,yid):
    global cnt
    
    print(f"Start Checking: xid,yid={xid},{yid}")
    if xid<0 or xid>=h or yid<0 or yid>=w:
        return

    if reached[xid][yid]:
        return

    reached[xid][yid] = True
    if A[xid][yid]==0:
        return
    A[xid][yid] = 0
    
    dfs(xid,yid-1)
    dfs(xid,yid)
    dfs(xid,yid+1)

    dfs(xid+1,yid-1)
    dfs(xid+1,yid)
    dfs(xid+1,yid+1)

    dfs(xid-1,yid-1)
    dfs(xid-1,yid)
    dfs(xid-1,yid+1)

for i in range(len(A)):
    for j in range(len(A[i])):
        print(i,j)
        if (i,j)==(0,0):
            print("IF")
            dfs(i,j)
            cnt+=1
        else:
            print(f"ELSE: {i}, {j}")
            print(f"A:{A}")
            if not reached and A[i][j]==1:
                dfs(i,j)
                cnt+=1

print(cnt)