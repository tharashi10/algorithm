'''Prime Numbers
素数判定
アイデア: N回割る必要はなく、sqrt(N)だけ割ってみて、
割り切れない場合は素数とみなすことができる。
例えばA=109であれば、10まで割ってみてダメなら素数と言ってOK
(計算量を減らせる)
'''
import math
A = int(input())

def isPrimeNumber(A):
    max_div = int(math.sqrt(A))
    cnt = []
    for i in range(2,max_div+1):
        if (A%i) == 0:
            cnt.append(i)
    if len(cnt) ==0:
        print(f"its not dividable.")
    for j in range(len(cnt)):
        print(f"dividable index is {cnt[j]}.")

isPrimeNumber(A)