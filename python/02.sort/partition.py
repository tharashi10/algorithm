""":
パーティション
あるリストに対し、最も右側にある値Xを基準として、
Xよりも小さい側と大きい側に分ける区分け線を見つけて出力する
(tooEasy)
Input
12
13 19 9 5 12 8 7 4 21 2 6 11
------
Output
9 5 8 7 4 2 6 [11] 21 13 19 12
"""

def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i+=1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]

    A_ = list(map(str,A))
    A_[i+1] = '['+ A_[i+1] +']'
    #print(*A_)
    return A_

if __name__ == "__main__":
    n = int(input())
    A =list(map(int, input().split()))
    p = 0
    print(*partition(A,p,n-1))