""":全探索(分割統治法)
Input()
5
1 5 7 10 21
4
2 4 17 8
--------
Output()
no
no
yes
yes
"""


# solve(i, m)を「i 番目以降の要素を使って m を作れる場合 true を返す」関数とする
def solve(i,m):
    # この分岐を入れないと、Testcase#10でTLEとなる
    # 配列要素を全部足してもmに届かない場合はその時点で探索をやめる
    if sum(A) < m:
        return False

    if m == 0:
        return True
    # iが探索対象の配列サイズを超えたらFalse
    if i >= N:
        return False
    # A[i]を使うか、使わないかで部分和問題となる
    result = solve(i+1,m) or solve(i+1,m-A[i])
    return result

if __name__ =="__main__":
    N = int(input())
    A = list(map(int, input().split()))
    #A = [int(input()) for _ in range(N)]
    q = int(input())
    M = list(map(int, input().split()))
    
    cnt = 0
    while(cnt<q):
        if solve(0,M[cnt]):
            print('yes')
        else:
            print('no')
        cnt+=1

        