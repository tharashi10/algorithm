n = int(input())
A = list(map(int,input().split()))

def bubbleSort(n,A):
    index = 0
    cnt = 0
    while(index<n):
        for i in reversed(range(index+1,n)):
            j = i-1
            if A[i] < A[j]:
                A[i],A[j]=A[j],A[i]
                cnt+=1
            #print("index: %s",i)
        index+=1
    print(*A)
    print(cnt)
bubbleSort(n,A)