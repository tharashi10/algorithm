n = int(input())
A = list(map(int,input().split()))

def selectionSort(n,A):
    for i in range(0,n)):
        min_idx = i
        cnt = 0
        for j in range(i,n)):
            if A[min_idx] > A[j]:
                min_idx=j
                A[min_idx],A[i]=A[i],A[min_idx]
                cnt+=1
            print("index: %s",i)
    print(*A)
    print(cnt)
selectionSort(n,A)