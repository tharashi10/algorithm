'''根付き木(rooted Tree)
根っこのNode(節点)を特別扱いする
ポイント:親子兄弟を表す構造体を用意する
状態遷移図（左子右兄弟関係）
--
print(sys.getrecursionlimit())
1000
判定時REとなる
'''
import sys
sys.setrecursionlimit(3**15)

# 構造体
# p:親, l:左Child, r:右Brother
# rとlは同じ深さにいない
class Node:
    def __init__(self,p,l,r):
        self.p = p
        self.l = l
        self.r = r

# 末端から根っこに向かって親がいるか探索していく
def get_depth(T,vid):
    '''
    T:Tree
    v:Node
    '''
    d = 0
    # 親がいる限りはひたすらループ
    while T[vid].p is not None:
        vid = T[vid].p #親ノードに移る
        d +=1

Depth = {}
# 根っこからスタートし、左→右の流れで検索していく
# v:節点のID
# q:現在いる深さ
# 深さのList Depth[]を生成する
def get_all_depth(Tree,vid,q):
    Depth[vid] = q
    # 兄弟いるなら横に移動
    if Tree[vid].r is not None:
        get_all_depth(Tree, Tree[vid].r, q)
    
    # 左下の子いるならに移動(深さIncrement)
    if Tree[vid].l is not None:
        get_all_depth(Tree, Tree[vid].l, q+1)

# ある節点(ノード)に対する子たちを返す
def return_children(Tree,vid):
    children = []
    c = Tree[vid].l
    while(c is not None):
        children.append(c)
        c = Tree[c].r #右がなくなるまで探索してる
    return children


n = int(input())

# リスト内包表記でDict作成
Tree = {id: Node(None,None,None) for id in range(n)}
# 標準入力値を整形する temp→Treeを作成
for _ in range(n):
    tmp = list(map(int,input().split()))
    if tmp[1] == 0: #　次数KがZeroの時
        continue # これ以降は処理しない
    vid = tmp[0]
    cl = tmp[2]
    Tree[vid].l = cl #親からみた子
    Tree[cl].p = vid #子からみた親
    tmp_sibling = tmp[2] #v1,v2...と見ていくがv1は既知なので保存しておく
    for sib in tmp[3:]:
        Tree[tmp_sibling].r = sib
        Tree[sib].p = vid
        tmp_sibling = sib

#print([Tree[i] for i in range[n]])

# 深さDepthリストを作る
for vid in range(n):
    if Tree[vid].p is None:
        get_all_depth(Tree, vid, 0) #開始点はRootのみ
        break

# 1ノードに対するPrint関数(出力形式に合わせる)
def print_single_node(Tree,vid,Depth):
    node_type = 'internal node' if Tree[vid].l is not None else 'leaf'
    if Tree[vid].p is None:
        parent = -1
        node_type = 'root'
    else:
        parent = Tree[vid].p
    children = return_children(Tree,vid)
    print(
        f'node {vid}: parent = {parent}, depth = {Depth[vid]}, {node_type}, {children}'
    )

for vid in range(n):
    print_single_node(Tree,vid,Depth)
