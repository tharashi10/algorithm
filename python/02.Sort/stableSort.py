"""
Input
5
H4 C9 S4 D2 C3
--------------
D2 C3 H4 S4 C9
Stable
D2 C3 S4 H4 C9
Not stable
"""

def selectionSort(n, A):
    cnt = 0
    for i in range(0,n):
        min_idx = i
        for j in range(i,n):
            if (A[min_idx])[1] > (A[j])[1]:
                min_idx=j
        A[min_idx],A[i]=A[i],A[min_idx]
        if (A[i])[1] < (A[min_idx])[1]:
            cnt+=1
    print(*A)

def bubbleSort(n, A):
    index = 0
    cnt = 0
    while(index<n):
        for i in reversed(range(index+1,n)):
            j = i-1
            if (A[i])[1] < (A[j])[1]:
                A[i],A[j]=A[j],A[i]
                cnt+=1
        index+=1
    print(*A)

def judgeStable(n, arr):
    l = []
    [l.append((arr[i])[0]) for i in range(len(arr))]
    for i in range(1,len(l)):
        stable = True
        if l[i] < l[i-1] and (arr[i])[1]==(arr[i-1])[1]:
            stable = False
            break
        else:
            continue
    if stable:
        print("Stable")
    else:
        print("Not stable")

if __name__ == "__main__":
    N = int(input())
    A = list(map(str,input().split()))
    B = A[:]
    # 参照IDを独立させる
    # print(id(A),id(B))
    bubbleSort(N,A)
    # バブルソートは安定
    print("Stable")

    selectionSort(N,B)
    print("Stable" if B == A else "Not stable")