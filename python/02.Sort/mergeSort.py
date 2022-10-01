'''分割統治法
マージソート
大きな配列を分割して、比較ソートして、
再びくっつけるイメージ。
input
---------
10
8 5 9 2 6 3 7 1 10 4
---------
1 2 3 4 5 6 7 8 9 10
34
'''

# 昇順に並び替える
def merge(A,left,mid,right):
    global count
    L = A[left:mid] + [1000000001]
    R = A[mid:right] + [1000000001]

    #以下の配列作成が原因で遅くなっていた(4.07secでTREになっていた)
    # n1 = mid - left
    # n2 = right - mid
    # L = [None]*n1
    # R = [None]*n2
    # 左側配列L、右側配列Rを作る
    # for i in range(0,n1):
    #    L[i] = A[left+i]
    # for i in range(0,n2):
    #    R[i] = A[mid+i]

    # L.append(float('inf'))
    # R.append(float('inf'))
    # L.append(1000000)
    # R.append(1000000)

    i = j = 0
    # LとRを比較していく
    # kは配列AのIndex用
    for k in range(left,right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i +=1
        else:
            A[k] = R[j]
            j +=1
    count+=(right-left)
        
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

if __name__ == "__main__":
    N = int(input())
    A = list(map(int,input().split()))
    count = 0

    left = 0
    right = N
    mid = (left+right)//2
    mergeSort(A,left,right)
    print(*A)
    print(count)