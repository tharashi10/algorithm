''':
最大ヒープ
Input
10
4 1 3 2 16 9 10 14 8 7
--------
Output
16 14 10 8 7 9 3 2 4 1
'''

def maxHeapify(A,i):
    # 再帰に入った瞬間に、Leftが存在することに留意する(図書くとわかる)
    # Nを2で割ってるので、Rightがあるかないかの2パターンがあるはず
    left = 2*i
    right = 2*i+1
    
    if left > n+1:
        return

    if A[left]>A[i]:
        largest = left
    else:
        largest = i

    if right <=n:
        if A[right]>A[largest]:
            largest= right
    
    if largest!=i:
        A[i],A[largest] = A[largest],A[i]
        maxHeapify(A,largest)

def buildHeap(A,n): 
    for i in reversed(range(1,n//2+1)):
        maxHeapify(A,i)
    return A

if __name__ == "__main__":
    n = int(input())
    A0 = ["None"]
    A1 = list(map(int,input().split()))
    
    A = A0+A1
    maxOrdered = buildHeap(A,n)
    l = maxOrdered[1:]
    print(' '+' '.join(map(str,l))) #ここの先頭空白部分は意外と盲点(Tipsへ追記)
