"""
壁をぶち壊す問題
In/
10 -10 1
Out/
10
--
In/
20 10 -10
Out/
40
---
B問題なのにあまり解けた気がしていない。
場合分けが甘い。X,Y,Zの3変数なので、丁寧に場合わけしないとNG。
ただ、X,Yの対称性を理解して、それを応用できたのは良かった。
"""

def solve(x,y,z):
    if x-y >=0 and y >=0:
        if y >=z:
            if z>=0:
                return x
            else:
                return 2*(-z)+x
            return x
        elif z>=y:
            return -1
        elif z>=0 and z<=y:
            return x
        else:
            return 2*(-z)+x
    else:
        return x

if __name__== "__main__":
    x, y, z = map(int,input().split())
    if x >=0:
        print(solve(x,y,z))
    else:
        print(solve(-x,-y,-z))
