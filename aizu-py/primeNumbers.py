'''Prime Numbers
素数判定
アイデア: N回割る必要はなく、sqrt(N)だけ割ってみて、
割り切れない場合は素数とみなすことができる。
例えばA=109であれば、10まで割ってみてダメなら素数と言ってOK
(計算量を減らせる)
'''
import math
N = int(input())
A = [int(input()) for _ in range(N)]
#x = int(input())

def isPrimeNumber(x):
    # 数学の知識を使う
    max_div = int(math.sqrt(x))
    if x==2:
        return True
    elif x<2 or x%2==0:
        return False
    
    i=3
    while(i<=max_div):
        if (x%i) == 0:
            return False
        i+=2
    
    return True

prime_num_cnt = 0
for i in range(N):
    if isPrimeNumber(A[i]):
        prime_num_cnt+=1
print(prime_num_cnt)