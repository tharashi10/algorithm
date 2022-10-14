""":最古の遺跡
実行時間:2922 ms (tuple()定義などの宣言を減らしまくった場合)
実行時間:3308 ms (tuple()でvec定義を入れた場合。6割TLEになる)
->この問題はかなり時間にシビア(C++ならもっと気にせずにACになると思う)

日本情報オリンピック本選考
10
9 4
4 3
1 1
4 2
2 4
5 8
4 0
5 3
0 5
5 2
"""

def setInput(): return tuple(map(int,input().split()))
n = int(input())
point_list = [setInput() for _ in range(n)]
square = 0
ll = set(point_list)

# in zip()は使うな.くそ遅い.TLEにならない
# setで、removeは使うな. 引数Checkのハンドリングめんどい
for i in range(n-1):
    for j in range(i+1,n):
        p1x,p1y = point_list[i][0],point_list[i][1]
        p2x,p2y = point_list[j][0],point_list[j][1]
        #vec = (p2x-p1x,p2y-p1y)
        #vertical = (-vec[1],vec[0])

        #ll = list(filter(lambda x: x not in [p1,p2], point_list))
        #ll.discard(p1)
        #ll.discard(p2) # setでは discard 使える
        p1_ = (p1x -(p2y-p1y), p1y + p2x-p1x)
        p2_ = (p2x -(p2y-p1y), p2y + p2x-p1x)

        if p1_ in ll and p2_ in ll:
            tmp = (p2x-p1x)*(p2x-p1x) + (p2y-p1y)*(p2y-p1y)
            if square <= tmp:
                square=tmp

print(square)
