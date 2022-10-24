"""
18:38
Pizza
方針
・店舗(d)の座標リストに対して、二分探索をし、宅配先(k)がどの店舗間にいるのかサーチする
・#18ではピュアな二分探索だったが、Whileの終了にて、どの店舗間にいるのかのIndexを返却する
・Bisect使いましょう
・本店のインデックス[0]を忘れずに入れましょう

実行時間: 180ms
Input---
8
3
2
3
1
4
6
Output---
3
"""
import bisect

# ACしないので、bisect使ってみる方針に変更
def bsearch(lst,x):
    left, right = 0, len(lst)
    while left< right:
        mid = (left+right)//2
        if x>lst[mid]:
            left = mid+1
        else:
            right = mid
    return mid-1,mid

d = int(input())
n = int(input())
m = int(input())
d_list = [0]

[d_list.append(int(input())) for _ in range(n-1)]
k_list = [int(input()) for _ in range(m)]

# 昇順にsortしておく
d_list.sort()

# 番兵として原点(本店)を入れておく
d_list.append(d)

distance = 0

for v in k_list:
    # Bisect使うと、挟まれる左右のIndexを取得できる
    idx = bisect.bisect_left(d_list,v)
    distance+=min(abs(d_list[idx-1]-v),abs(d_list[idx]-v))

    #p = k_list[ii]
    #print(f"x: {p}")
    #p1,p2 = bsearch(d_list,p)
    #print(f"p1,p2: {p1},{p2}")
    #print(min(abs(d_list[p1]-p),abs(d_list[p2]-p)))
    #distance+=min(abs(d_list[p1]-p),abs(d_list[p2]-p))

print(distance)
