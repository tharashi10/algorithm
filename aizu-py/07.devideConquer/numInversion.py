""":
反転数を計算; The Number of Inversion
※バブルソートの交換回数は反転数または転倒数と呼ばれるもので、列の乱れの具合を表す数値でもある
--
SimpleなBubbleSortだと、N=100,000でTLE(4.99 sec)となる。
→Merge Sortを利用する(分割後、反転数の和をとるイメージ)
Input
5
3 5 2 1 4
---------
6
追記)純粋にMerge Sortの比較カウントをするだけでは解けない。
あくまでもここで聞かれているのは、反転回数。
L > Rとなっている場合に、L側の残存要素数を計算する。
(ソート済みのLRをマージする時に遷移図書けばわかる)

左右の部分列の要素を先頭から順に比較し、
小さいものをソート先の配列に格納するのがマージの手順です。
右の部分列の要素の方が左の部分列の要素よりも小さいとき、
左の部分列の要素のうち残されているものの数をカウントします。
(https://programgenjin.hatenablog.com/entry/2019/04/25/143708)
"""

# Conquerのステップ（Upwards）
def merge(A,l,mid,r):
    global count
    L = A[l:mid] + [1000000001] #[1000000001]は番兵さん
    R = A[mid:r] + [1000000001] #[1000000001]は番兵さん
    
    # i: L's Index
    # j: R's Index
    i=j=0
    # 部分配列を配列Aとしてくっつけてあげる
    for k in range(l,r):
        # 左要素よりも右要素の方が大きい場合は反転のカウントアップをしない
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            # 左要素よりも右要素の方が小さい場合は左の要素数だけ反転のカウントアップをする
            A[k]=R[j]
            j+=1
            #print("----")
            #print(mid,(mid-i))
            # lは常に0オリジンではない。スタート地点は変わるので、L側の個数（または0オリジンの最大Index）が必要
            l_num = mid - l
            count+=l_num-i

def mergeSort(A,l,r):
    if (l+1) <r:
        mid = (l+r)//2
        mergeSort(A,l,mid)
        mergeSort(A,mid,r)
        merge(A,l,mid,r)

if __name__=="__main__":
    n = int(input())
    A = list(map(int,input().split()))
    count = 0
    mergeSort(A,0,n)
    print(count)