'''ヒープソート
降順にして最大ヒープを求める。
その後、最大値をO(1)で取り出して行って昇順に並べる
'''
n = int(input())
A = list(map(int,input().split()))

def maxheap(A,n,trg):
    left = 2*trg + 1
    right = left + 1
    max_idx = trg

    #左の子がいれば
    if left < n:
        if A[trg] < A[left]:
            max_idx = left
    #右の子がいれば
    if right < n:
        if A[trg] < A[right]:
            max_idx = right
    if trg != max_idx:
        A[trg],A[max_idx] = A[max_idx],A[trg]
        maxheap(A,n,max_idx)

# Maxheapを作成する
def build_heap(A):
    n = len(A)
    for i in range(n//2,-1,-1):
        maxheap(A,n,i)
        print(A)

def heap_sort(A,n):
    build_heap(A,n)
    for i in range(n-1,0,-1):
        A[i],A[0] = A[0],A[i]
        maxheap(A,i,0)

build_heap(A)
#heap_sort(A,n)
#print(A)