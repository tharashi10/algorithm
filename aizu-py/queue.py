''':Queue
CPUの処理サンプルTODO
'''
class CpuQueue:
    def __init__(self,head,tail,n,lst):
        self.head = head
        self.tail = tail
        self.n = n
        self.lst = lst
        print(head)
        print(tail)

    def isEmpty(self):
        return self.head==self.tail

    def isFull(self):
        # 配列が"0 Origin"なので+1
        return self.head==(self.tail+1)%self.n

    def enqueue(self,x):
        if self.isFull():
            print("Overflow...")
        self.lst[self.tail] = x
        if self.tail+1 == self.n:
            self.tail = 0
        else:
            self.tail+=1
    
    def dequeue(self):
        if self.isEmpty():
            print("Underflow...")
        tmp = self.lst[self.head]
        if self.head+1 == self.n:
            self.head = 0
        else:
            self.head+=1
        return tmp

def solver():
    n,t = map(int,input().split())
    queue = []
    for i in range(n):
        a,b = input().split()
        queue.append([a,int(b)])
    lst = queue
    cq = CpuQueue(head=0,tail=n-1,n=n,lst=lst)
    cnt = 0
    while(not cq.isEmpty()):
        if queue[cq.head][1] >100:
            queue[cq.head][1]-=100
            #cq.dequeue()
            #queue[cq.head][1]-=100
            cq.enqueue(queue[cq.head])
            print(queue)
            print("---")
        else:
            cq.dequeue()
        cnt+=1
    print(cnt)
    print(queue)

if __name__ == "__main__":
    solver()