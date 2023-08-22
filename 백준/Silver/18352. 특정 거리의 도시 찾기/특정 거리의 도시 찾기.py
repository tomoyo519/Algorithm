import sys
input = sys.stdin.readline
from collections import deque
N, L, K, S = map(int, input().split())

graph = [ [] for _ in range(N+1)]
for _ in range(L):
    x, y = map(int, input().split())
    graph[x].append(y)
queue = deque()
distance = [-1] * (N +1) # 노드간 거리 -1 로 초기화
distance[S] = 0 #시작 노드의 거리는 0으로

def bfs(S):
   
    queue.append(S)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if distance[i] == -1:
                distance[i] = distance[v]+1
                queue.append(i)
                
    tf =False
                
    # print(distance)
    for k in range(1,len(distance)):
        if distance[k] == K:
            print(k)
            tf=True
            
    if tf ==False:
        print(-1)

bfs(S)  

