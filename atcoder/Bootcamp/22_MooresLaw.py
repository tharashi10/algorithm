""":
ムーアの法則
方針: 二分法を用いる
a<b で、f(a)>0 かつ f(b)<0 の時に、
f(x)=0の解が近似的に求まる。
https://risalc.info/src/bisection-method.html

方針（追記)
・関数の極値は三分探索（微分しないで解くならば）
・1回微分すると、f'は単調増加関数になる(f"で下に凸な関数と分かる)
・解くのにかかる時間は calc = mid + p/(2**(mid/1.5))

In 3.0000
Out 2.8708930019
P は実数で、小数点以下第 4 位まで与えられる
----
"""

import math
p = float(input())

eps1 = 0.00001
eps2 = 0.00001

def f(x):
    return x + p*(2**(-x/1.5))

def g(x):
    return 1 + p*(math.log(2**(-1/1.5)))*(2**(-x/1.5))

def bisect_func(left,right):
    n = 5000
    while(True):
        mid = (left + right)/2
        #print("{}\t{:.5f}\t{:.5f}\t{}\t{}".format(n, mid, g(mid), left,right))
        if g(mid) <= 0:
            left = mid
        else:
            right = mid
        n-=1
        if n==0:
            break
        #if abs(g(mid)) < eps1 or abs(left - right) < eps2:
            #break
    return mid

print(f(bisect_func(0,p)))