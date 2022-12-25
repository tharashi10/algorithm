"""
Greedy
自力ACできた
Greedyはシンプル
2 3 3
0 2
"""

"""
貪欲法で書き直す
"""
def main():
    A,B,K = map(int,input().split())
    eat = min(A,K)
    A-=eat
    K-=eat

    eat = min(B,K)
    B-=eat
    K-=eat

    print(f"{A} {B}")

if __name__=="__main__":
    main()


"""
# ゴリ押しでACしたやつ(計算量的にはOK)
def main():
    A,B,K = map(int,input().split())
    
    if A<=B:
        if A+B<=K:
            print(f"0 0")
        if A<=K<(A+B):
            print(f"0 {B-(K-A)}")
        if K<A:
            print(f"{A-K} {B}")
    else:
        if K<A:
            print(f"{A-K} {B}")
        if A<=K<(A+B):
            print(f"0 {B-(K-A)}")
        if (A+B)<=K:
            print(f"0 0")

if __name__ == "__main__":
    main()
"""