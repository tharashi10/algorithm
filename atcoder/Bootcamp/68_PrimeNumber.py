"""
素因数分解
https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8

ポイント
・出力にやや癖あり。print(' '.join(map(str,l)))) 使った
・高速素数判定を使う中で、エラトステネス的に割り算トライのWhile Loopを回す

12
12: 2 2 3
"""
import math

# 目標は [[素因数,回数(指数)]]
def main():
    N = int(input())

    def prime_factorize(x):
        factorize_array = []
        max_div = int(math.sqrt(x))
        if x==1:
            return None
        
        for i in range(2,max_div+1):
            if x%i==0:
                cnt=0
                while x%i==0: # iで何回割れるか調査
                    cnt+=1
                    x = x//i
                factorize_array.append([i,cnt])
        
        # ex. 26で2で割れた後、x=13としてこのIF判定に入る
        if x!=1:
            factorize_array.append([x,1])

        return factorize_array
    
    factorize_array = prime_factorize(N)
    ans = []
    for i in range(len(factorize_array)):
        for _ in range(factorize_array[i][1]):
            ans.append(factorize_array[i][0])
    
    print(f"{N}: {' '.join(list(map(str, ans)))}")

if __name__=="__main__":
    main()
