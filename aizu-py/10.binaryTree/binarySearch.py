'''二分探索(境目をみつける)
制約:Sの要素は昇順に整列されている
'''

def binarySearch(x,lst):
    # 切り捨て除算 //
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