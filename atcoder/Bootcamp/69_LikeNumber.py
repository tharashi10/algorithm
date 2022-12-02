"""
普通に素数判定していけばいい気がする
→しっかりTLEでハマった。そんな簡単じゃなかった。
→時間内ACのためには、エラトステネスの篩を実装しないといけないっぽい
https://img.atcoder.jp/abc084/editorial.pdf

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
    V = 10**5
    Primes = [True]*(V+1)
    Primes[0]=Primes[1]=False
    for i in range(2,V+1):
        for j in range(i*2,V+1,i):
            Primes[j]=False

    CumSum = [0]*(V+1) # 1以上x以下の「2017に似た数」の個数を格納する配列
    
    for i in range(1,V+1,2): # 2以外で、偶数は素数になり得ないので、奇数のみLoop
        query = (i+1)//2
        if Primes[i] and Primes[query]:
            CumSum[i]+=1

    for i in range(1,V):
        CumSum[i+1]+=CumSum[i]
    
    for _ in range(N):
        s,t=map(int,input().split())
        print(CumSum[t]-CumSum[s-1])
    
    #print(CumSum[:20])

if __name__=="__main__":
    main()
