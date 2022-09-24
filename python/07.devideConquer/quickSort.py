"""
QuickSort
(Divide Conquer)
---
Input
6
D 3
H 2
D 1
S 3
D 2
C 1
---
Output
Not stable
D 1
C 1
D 2
H 2
D 3
S 3
"""
#from collections import namedtuple

def partition(A,p,r):
    x = A[r][1]
    i = p-1
    for j in range(p,r):
        if A[j][1] <= x:
            i+=1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    # partitionのIndexを返す
    return i+1

def quicksort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)

        # Partition's IndexはSkip
        quicksort(A,q+1,r)

if __name__ == "__main__":
    n = int(input())
    A = [[kind,int(num)] for kind,num in (list(input().split()) for _ in range(0,n))]
    list_stable = sorted(A, key=lambda x:x[1])
    quicksort(A,0,n-1)
    if A==list_stable:
        print("Stable")
    else:
        print("Not stable")
    
    i=0
    while i<n:
        print("%s %s" %(A[i][0],A[i][1]))
        i+=1
    #print(*A)
