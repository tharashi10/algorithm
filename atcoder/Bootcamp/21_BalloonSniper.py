"""
Balloon Sniper
方針: 最小値問題ではなく、判定問題に読み替える
二分探索を使うタイミング: Xの値(連続な整数)を左右から狭めていって、
判定を行なっていって、最終的にOK/NGとなる閾値がもとまる。(この閾値を求めるのに使う)
Input
4
5 6
12 4
14 7
21 2
Output
23
"""

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int,input().split())))

# スコア値Xの時に、ちゃんと全部の風船を割ることができるか判定
def check(x):
    x_list = []
    for i in range(n):
        time_limit = (x - l[i][0])//l[i][1]
        x_list.append(time_limit)
    x_list.sort()
    
    for j in range(n):
        if x_list[j] < j:
            return False
    return True

def bisect_func(left,right):
    while (right-left > 1):
        mid = (left+right)//2
        if check(mid):
            right = mid
        else:
            left = mid
    return right

m = 10**18
print(bisect_func(0,m))