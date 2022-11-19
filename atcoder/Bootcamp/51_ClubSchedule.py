"""
クラブ活動のスケジュール
2
OI
7
「注目すべきは、i 日目の出席者を決めたとき、
i + 1 日目の出席者を決める際には、1 日目から i - 1 日目まで
誰が出席するかは関係ないということである」と解説にある。
JOIの解説は、文面上わかりやすい
https://www.ioi-jp.org/joi/2013/2014-yo/2014-yo-t4/review/2014-yo-t4-review.html
https://www.hackerearth.com/practice/algorithms/dynamic-programming/bit-masking/tutorial/

dp[JOIの集合][i日目]=i日目までのスケジュールの決め方の総和(i日目に参加者の集合がSとなる時)
初期状態dp[J][0日目]=1  : Jが1番初めに部室の鍵を持っているので0日目で定義


000 = {     } : 0
001 = {    I} : 1
010 = {  O  } : 2
011 = {  O I} : 3
100 = {J    } : 4 -> 1<<2
101 = {J   I} : 5
110 = {J O  } : 6
111 = {J O I} : 7

"""

def main():
    N = int(input())
    st = str(input())
    M = [2 if st[k]=='J' else 1 if st[k]=='O' else 0 for k in range(N)]

    dp = [[0]*(N+1) for _ in range(1<<3)]
    dp[4][0] = 1
    
    for i in range(0,N): # i=0,1
        for now in range(1<<3):
            for next in range(1<<3):
                if (next & now) != 0: # AND条件でφにならない
                    if (next >> M[i]) &1 ==1: # 責任者がちゃんと含まれる
                        dp[next][i+1]+=dp[now][i]
                        #print(f"test: i,now,next: {i},{now},{next}")
    
    ans=sum([(dp[i][N]) for i in range(1<<3)])
    print(ans%10007)

if __name__ =="__main__":
    main()
