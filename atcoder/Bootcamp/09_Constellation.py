""" D - 星座探し
平行移動の範囲を正方形で考えると小さいテストケースでは解を得られるが、TLEになる。
そのため、考え方の方針としては、ある星座に着目し、写真のN個のどれかひとつに重なるように
平行移動を決めていけば良い。そうすると、高々N個しか平行移動パターンはないとすることができる
---Input
5
8 5
6 4
4 3
7 10
0 10
10
10 5
2 7
9 7
8 10
10 2
1 2
8 1
6 7
6 0
0 9
---Output
2 -3
"""

xy = []
XY = []
n = int(input())
for i in range(n):
    xy.append(tuple(map(int,input().split())))

m = int(input())
for i in range(m):
    XY.append(tuple(map(int,input().split())))

SS = set(XY)
px, py = xy[0][0],xy[0][1]
vec = [(XY[i][0]-px,XY[i][1]-py) for i in range(m)]
#print(px,py,vec)

for i in range(len(SS)):
    ss = set((map(lambda x:(x[0]+vec[i][0],x[1]+vec[i][1]), xy)))
    if ss.issubset(SS):
        print(f"{vec[i][0]} {vec[i][1]}")
        break