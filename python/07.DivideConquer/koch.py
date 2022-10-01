""":
コッホ曲線
再帰関数を利用する
入力はNのみ。
"""
import math
from collections import namedtuple

def koch(n,p1,p2):
    if n==0:
        return
    
    p1_x = p1.x
    p1_y = p1.y
    p2_x = p2.x
    p2_y = p2.y

    # p1, p2からs,t,uを計算
    s = Point((2*p1_x + p2_x)/3,(2*p1_y + p2_y)/3)
    t = Point((p1_x + 2*p2_x)/3,(p1_y + 2*p2_y)/3)

    # ここの式を間違えないよう気を付ける
    # import cmathで回転座標変換も可能
    ux = (t.x-s.x)*math.cos(math.radians(60)) - (t.y-s.y)*math.sin(math.radians(60))+s.x
    uy = (t.x-s.x)*math.sin(math.radians(60)) + (t.y-s.y)*math.cos(math.radians(60))+s.y
    u = Point(ux,uy)

    koch(n-1,p1,s)
    print("{0:.8f} {1:.8f}".format(*s))

    koch(n-1,s,u)
    print("{0:.8f} {1:.8f}".format(*u))

    koch(n-1,u,t)
    print("{0:.8f} {1:.8f}".format(*t))

    koch(n-1,t,p2)
    #print(*p2)


if __name__ == "__main__":
    n = int(input())
    Point = namedtuple("Point",('x','y'))
    p1 = Point(0,0)
    p2 = Point(100,0)
    print("{0:.8f} {1:.8f}".format(*p1))
    
    koch(n, p1, p2)
    print("{0:.8f} {1:.8f}".format(*p2))