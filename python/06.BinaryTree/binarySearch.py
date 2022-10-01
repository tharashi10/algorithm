'''二分探索(境目をみつける)
n 個の整数を含む数列 S と、q 個の異なる整数を含む数列 T を読み込み、
T に含まれる整数の中で S に含まれるものの個数 C を出力するプログラムを作成する
制約:Sの要素は昇順に整列されている
Input
5
1 2 3 4 5
3
3 4 1
------
Output
3
'''


def binarySearch(x,lst):
    left = 0
    right = len(lst)
    flag = 0
    while(left<right):
        mid = (left+right)//2
        if lst[mid]==x:
            flag = 1
            break
        elif x > lst[mid]:
            left = mid + 1
        else :
            right = mid
    return flag

n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

cnt = 0
for idx in range(0,len(T)):
    if binarySearch(T[idx],S)==1:
        cnt+=1

print(cnt)