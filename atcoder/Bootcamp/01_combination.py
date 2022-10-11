""":01
重複無しで「３つ」の数を選びそれらの合計が x となる組み合わせの数
In: 5 9
    0 0
Out: 2
実行速度:01.20 s
"""

while True:
    n,s = map(int,input().split())
    if n==0:
        break
    # 全探索する
    # i < j < k とする
    cnt = 0
    lst =[i for i in range(1,n+1)]
    
    for i in lst:
        tmp1 = s
        lst1 = list(filter(lambda x : x>i, lst))
        tmp1-=i
        
        for j in lst1:
            tmp2 = tmp1
            lst2 = list(filter(lambda x : x>j, lst1))
            tmp2-=j

            for k in lst2:
                tmp3 = tmp2
                tmp3-=k
                if tmp3 ==0:
                    cnt+=1
                    #print(i,j,k)
    print(cnt)
