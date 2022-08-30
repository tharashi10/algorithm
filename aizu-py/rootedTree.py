'''根付き木(rooted Tree)
根っこのNode(節点)を特別扱いする
ポイント:親子兄弟を表す構造体を用意する
状態遷移図（左子右兄弟関係）
'''
# p:親, l:左Child, r:右Brother
# rとlは同じ深さにいない
class Node:
    def __init__(self,p,l,r):
        self.p = p
        self.l = l
        self.r = r

# 末端から根っこに向かって親がいるか探索していく
def get_depth(T,v):
    '''
    T:Tree
    v:Node
    '''
    d = 0
    while T[v].p is not None:
        v = T[v].p
        d +=1

Depth = {}
# 根っこからスタートし、左→右の流れで検索していく
# v:節点のID
# p:現在いる深さ
def get_all_depth(Tree,v,p):
    Depth[v] = p
    if Tree[v].r is not None:
        get_all_depth(Tree, Tree[v].r, p)
    if Tree[v].l is not None:
        get_all_depth(Tree, Tree[v].l, p+1)

# ある節点(ノード)に対する子を返す
def return_children(Tree,v):
    children = []
    while(Tree[v].l is not None):
        children.append(Tree[v].l)
        c = Tree[v].r
    return children


n = int(input())
# lambdaで
Tree = {id: Node(None,None,None) for id in range(n)}
for _ in range(n):
    tmp = list(map(int,input().split()))
    if tmp[1] == 0: #次数がZero
        continue
    Tree[tmp[0]].l = tmp[2]
    Tree[tmp[2]].p = tmp[0]
    tmp_sibling = tmp[2]
    for sib in tmp[3:]:
        Tree[tmp_sibling].r = sib
        Tree[sib].p = tmp[0]
        tmp_sibling = sib

for node in range(n):
    if Tree[node].p is None:
        get_all_depth(Tree, node, 0) #開始点はRootのみ
        break
#
#for node in range(n):
#    node_type = 