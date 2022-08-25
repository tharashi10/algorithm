n = int(input())
A = list(map(int,input().split()))

def selectionSort(n,A):
    cnt = 0
    for i in range(0,n):
        min_idx = i
        for j in range(i,n):
            if A[min_idx] > A[j]:
                min_idx=j
        A[min_idx],A[i]=A[i],A[min_idx]
        if A[i] < A[min_idx]:
            cnt+=1
    print(*A)
    print(cnt)
selectionSort(n,A)