'''Treeの再構築
PreOrder と InOrderから部分木を作って再起的に二分木を構築する
方針:
1.PreOrderから根Nodeを発見する
2.発見したNodeに対して、InOrderを左部分木と右部分木に分ける
3.左部分木と、右部分木でPreOrderを作成する
4.作成したPreOrderと部分木をInputにして、1.の手番を始める(再帰)
----
Input
5
1 2 3 4 5
3 2 4 1 5
--
Output
3 4 2 5 1
'''

class Node:
    def __init__(self,parent,left,right):
        self.parent = parent
        self.left = left
        self.right right

def reconst(subtree_L,subtree_R):
    if len(subtree_L)<=1 or len(subtree_R)<=1:
        return

if __name__ == "__main__":
    n = int(input())
    pre_order = list(map(int,input().split()))
    in_order = list(map(int,input().split()))
    
    reconst(pre_order,in_order)
    