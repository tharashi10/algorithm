'''
ソートプログラム
'''
n = int(input())
A = list(map(int,input().split()))

def sortAsc(n, A) -> None:
    print(*A)
    for i in range(1,n):
        tmp = A[i]
        j = i-1
        while(A[j] > tmp and j >= 0):
            A[j+1] = A[j]
            j-=1
        
        A[j+1] = tmp
        print(*A)

# Unpack List(*)
sortAsc(n,A)