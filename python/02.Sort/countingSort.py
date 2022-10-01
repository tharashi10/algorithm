''':
計数ソート
入力
7
2 5 1 3 2 3 0
--------------
出力
0 1 2 2 3 3 5
'''

def countingSort(A, B, N, k):
    for j in range(N):
        C[A[j+1]]+=1
    
    #累積和をとる
    for i in range(1,k+1):
        C[i] +=C[i-1]
    #print(C[0:5])

    for j in reversed(range(0,N)):
        B[C[A[j+1]]] = A[j+1]
        C[A[j+1]]-=1

    print(*B[1:])

if __name__ == "__main__":
    N = int(input())
    # Noneを入れてIndexを合わせる
    # ここハマった
    A = [None] + list(map(int,input().split()))
    k = 10000
    B = [None]*(N+1)
    C = [0]*(10001)
    countingSort(A,B,N,k)
