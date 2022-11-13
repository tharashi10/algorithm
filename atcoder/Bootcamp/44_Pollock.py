"""
ポロック予想
・PythonでTLEしない方法が果たしてあるのだろうか.と言う感じ
・重複DPとしてとく
Input--
40
14
5
165
120
103
106
139
0
Output--
2 6
2 14
2 5
1 1
1 18
5 35
4 4
3 37

dp[i][j] := i番目までの数を使うとして、和がjとなる場合の正四面体の最小個数
odd[i][j] :奇数のみ計算に使う場合 

正四面体の個数
m=0,cal(m)=0
m=1,cal(m)=1
m=2,cal(m)=4
m=3,cal(m)=10
m=4,cal(m)=20
m=5,cal(m)=35
m=6,cal(m)=56
m=7,cal(m)=84
m=8,cal(m)=120
m=9,cal(m)=165

dp[使う数の個数][狙う和]
|-0 1 2 3 4 5 6 7 8 9
|-縦は和------------------
| 0 0 0 0 0 0 0 0 0 0  <- この行では何も使わないので当然0
| 0 1 2 3 4 5 6 7 8 9  <- m=1のみ使うとき. 1(1個),1+1(2個),1+1+1(3個)....
| 0 1 2 3 1 2 3 4 2 3  <- m=1とm=4のみ使う. ex.狙う和が8なら、4+4(2個)
| 0 0 0 0 0 0 0 0 0 0  <- m=1とm=4とm=10を使う.

dp[2][8] = min(dp[1][8], dp[2][8-`4`]+1) 

--------------------
"""

def cal(x):
    return int(x*(x+1)*(x+2)/6)

MAX = 10**5
dp = []
odd = []
for i in range(MAX):
    dp.append(1000)
    odd.append(1000)

dp[0]=0
odd[0]=0
for i in range(1000):
    num = cal(i)
    for j in range(MAX):
        if j-num>=0:
            dp[j]=min(dp[j],dp[j-num]+1)
        if num&1 and j-num>=0:
            odd[j]=min(odd[j],odd[j-num]+1)

while True:
    n = int(input())
    if n==0:
        break
    print(f"{dp[n]} {odd[n]}")

""" Ref
base=[i*(i+1)*(i+2)//6 for i in range(2,181)]
odd_base=[i for i in base if i%2==1]

def pollock(base):
    dp=list(range(10**6))
    for i in base:
        for j in range(i,10**6):
            if dp[j]>dp[j-i]+1:
                dp[j]=dp[j-i]+1
    return dp

l1=pollock(base)
l2=pollock(odd_base)

def main(l):
    for i in l:
        print(l1[i],l2[i])

if __name__=="__main__":
    l=[]
    for _ in range(10**6):
        i=int(input())
        if i==0:
            break
        l.append(i)
    main(l)
    exit()
"""