"""
二分法: 条件を満たす範囲と満たさない範囲を二つに分けて、中間を見つけていく方法
入力
5 3
8
1
7
3
9
------
出力
10
"""

def check(P, arr, k):
    #あるTruckの重さ合計;weight
    #Truckの個数;truck_num
    weight = 0
    truck_num = 1
    for i, m in enumerate(arr):
        if m > P:
            return i #i個まで乗せることが可能

        if weight+m <= P:
            weight +=m
        else:
            truck_num+=1
            weight=m

        if truck_num == k+1:
            return i

    return len(arr)

def bisection_binarysearch(arr,k,n):
    # left, right:P最大積載量
    left = 0
    right = 100000*100000
    while(right-left > 1):
        mid = (left + right)//2
        # check()はindexを戻す(余裕がある場合、arrの大きさを戻す)
        if check(mid, arr, k)>=n:
            right = mid
        else:
            left = mid
    return right

if __name__ == "__main__":
    n, k= map(int, input().split())
    w = []
    for _ in range(n):
        w.append(int(input()))
    #print(w)
    print(bisection_binarysearch(w,k,n))
