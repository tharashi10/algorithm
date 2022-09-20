""":
ShellSort
---
入力
5 
5
1
4
3
2
---
出力
2
4 1
3
1
2
3
4
5
---
1 行目に整数 m、2 行目に m 個の整数 Gi(i=0,1,...,m−1) を空白区切りで出力してください。
3 行目に、G を用いた場合のプログラムが終了した直後の cnt　の値を出力してください。
続く n 行に整列した Ai(i=0,1,...,n−1) を出力してください。 
"""

def insertionSort(A,n,g):
    count = 0
    for i in range(g,n):
        tmp = A[i]
        j = i-g
        while(A[j] > tmp and j >= 0):
            A[j+g] = A[j]
            j-=g
            count+=1
        A[j+g] = tmp
    return count

def shellsort(A,n):
    m = int.bit_length(n)
    G = [n//(2**i) for i in range(m)]
    #print("----")
    print(m)
    print(*G)

    cnt=0
    for i in range(m):
        cnt+=insertionSort(A,n,G[i])
    print(cnt)
    [print(A[i]) for i in range(len(A))]

if __name__=="__main__":
    n = int(input())
    A = [int(input()) for _ in range(n)]
    shellsort(A,n)