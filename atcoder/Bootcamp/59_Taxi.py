"""
Taxi 

6 6
400 2
200 1
600 3
1000 1
300 5
700 4
1 2
2 3
3 6
4 6
1 5
2 4
--
700
"""

"""
    import heapq
    import collections
     
    def main():
        N,K = map(int,input().split())
        CR = [[0,0]]+[ list(map(int,input().split())) for _ in range(N) ]
     
        # グラフ作成
        graph = [ [] for _ in range(N+1) ]
        for i in range(K):
            A,B = map(int,input().split())
            graph[A].append(B)
            graph[B].append(A)
     
        # コストを加味したグラフ作成
        new_graph = [ [] for _ in range(N+1) ]
        for i in range(1,N):
            dist = [-1]*(N+1)
            dist[i]=0
            queue = collections.deque()
            queue.append(i)
     
            while queue:
                q = queue.popleft()
     
                if not graph[q]:
                    continue
                for x in graph[q]:
                    if dist[x] == -1:
                        dist[x] = dist[q]+1
                        if dist[x]<=CR[i][1]:
                            new_graph[i].append(x)
                            queue.append(x)
     
        #メモリ解法
        del graph,queue
     
        # ダイクストラ法
        heap = []
        heapq.heappush(heap,(0,1))
        dist = [1e20]*(N+1)
        seen = [False]*(N+1)
     
        while heap:
            pre_cost,pre = heapq.heappop(heap)
            if seen[pre]:
                continue
            seen[pre]=True
     
            cost = CR[pre][0]
            for to in new_graph[pre]:
                if seen[to]==False and dist[to]>pre_cost+cost:
                    dist[to] = pre_cost+cost
                    heapq.heappush(heap,(dist[to],to))
        print(dist[N])
     
    if __name__=='__main__':
        main()
        """