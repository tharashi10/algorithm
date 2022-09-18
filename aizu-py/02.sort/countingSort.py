''':
計数ソート
入力
7
2 5 1 3 2 3 0
--------------
出力
0 1 2 2 3 3 5
'''

def countingSort(A, B, N):
    for i in range(N):
        C[i] = 0
    for j in range(N):
        C[A[j]] +=1
    #累積和をとる
    for k in range(1,N):
        C[i] = C[i] + C[i-1]
    
    for l in reversed(range(0,N)):
        B[C[A[j]]] = A[j]
        C[A[j]]=-1

