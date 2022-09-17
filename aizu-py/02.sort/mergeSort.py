'''分割統治法
マージソート
大きな配列を分割して、比較ソートして、
再びくっつけるイメージ。
トップダウン
'''
N = int(input())
A = list(map(int,input().split()))
count = 0

# 昇順に並び替える
def merge(A,left,mid,right):
    global count
    n1 = int(mid - left)
    n2 = int(right - mid)
    L = [None]*n1
    R = [None]*n2

    # 左側配列L、右側配列Rを作る
    for i in range(0,n1):
        L[i] = A[left+i]
    for i in range(0,n2):
        R[i] = A[mid+i]

    #print(L)
    #print(R)
    L.append(float('inf'))
    R.append(float('inf'))

    i = 0
    j = 0
    # LとRを比較していく
    # kは配列AのIndex用
    for k in range(left,right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i +=1
            count+=1
        else:
            A[k] = R[j]
            j +=1
            count+=1
        
# 配列を二つに分割して、配列が1つになるまで再帰的に比較する
# 加えて、比較をしたのち配列を昇順に並び変える
def mergeSort(A,left,right):
    if left +1 < right:
        mid = (left + right)//2
        mergeSort(A,left,mid)
        mergeSort(A,mid,right)

        # midを境にして分割した配列をソートする
        # merge()後、Aがソートされている
        merge(A,left,mid,right)

left = 0
right = N
mid = (left+right)//2

mergeSort(A,left,right)
print(*A)
print(count)