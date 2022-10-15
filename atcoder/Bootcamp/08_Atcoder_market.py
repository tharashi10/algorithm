""":B - AtCoder Market
全探索めちゃめちゃ学んだ。こいつは勉強になる。すぐ答えを見ない方がいい(気づきが減るため)
(1) 道筋は、いつも S-> Ai -> Bi -> T の順序となる
(2) i,jでN*N通り。かつ、(1)のStep計算でN通りあるので最大でも 計算量は N*N*N になる
---Input
3
5 7
2 6
8 10
---Out
18

実行時間: 34 ms
"""
n = int(input())
lst = []
distance = 10000000000000

for _ in range(n):
    lst.append(list(map(int,input().split())))

for i in range(n):
    s = lst[i][0]
    for j in range(n):
        t = lst[j][1]
        d = 0
        for k in range(n):
            d += (abs(lst[k][0]-s) + abs(lst[k][0]-lst[k][1]) + abs(t-lst[k][1]))
        if d < distance:
            distance = d
            #print(f"{s},{t},{distance} steps")

print(distance)