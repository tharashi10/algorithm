''':Queue
CPUの処理サンプル
'''
n,t = map(int,input().split())
list = []
for i in range(n):
    a,b = input().split()
    list.append((a,int(b)))

def isEmpty(head_idx, tail_idx):
    return head_idx==tail_idx

def isFull(n, head_idx, tail_idx):
    # 配列が"0 Origin"なので+1
    return head_idx==(tail_idx+1)%n

def enqueue(lst, n, head_idx, tail_idx):
    if isFull(n, head_idx, tail_idx):
        print("Overflow...")
    
    if lst

print(list)