"""
普通に素数判定していけばいい気がする
→しっかりTLEでハマった。そんな簡単じゃなかった。
→時間内ACのためには、エラトステネスの篩を実装しないといけないっぽい

4
13 13 
7 11
7 11
2017 2017
--
1
0
0
1
"""

import math
def main():
    N = int(input())
    V = 10*5
    Primes = [True]*(V+1)
    Primes[0]=Primes[1]=False
    for i in range(2,V+1):
        for j in range(i*2,V+1,i):
            Primes[j]=False

    CumSum = [0]*(V+1) # とある値までに、何個素数があるかを格納する配列
    CumSum[1] = 1 # 便宜上1にしてみる
    for i in range(3,V+1,2): # 2以外で、偶数は素数になり得ないので、奇数のみLoop
        if Primes[i]:
            CumSum[i] = CumSum[i-2]+1
        
        query = (i+1)//2
        if Primes[query]:
            CumSum[i]+=1
            CumSum[tmp]=CumSum[tmp-2]+1

    for _ in range(N):
        A.append(list(map(int,input().split())))
    
    def isPrime(x):
        max_div = int(math.sqrt(x))
        if x==2:
            return True
        
        if x%2==0 or x==1:
            return False
        
        i = 3
        while i <= max_div:
            if x%i==0:
                return False
            i+=2

        return True
    
    for i in range(N):
        cnt = 0
        start = int((A[i][0]+1)/2)
        end = start+int((A[i][1]-A[i][0])/2)+1
        
        for j in range(start,end):
            if isPrime(2*j-1) and isPrime(j):
                cnt+=1
    
        print(cnt)

if __name__=="__main__":
    main()
