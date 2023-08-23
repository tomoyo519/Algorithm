import sys
import heapq
input = sys.stdin.readline

node = int(input())
busNum = int(input())
graph=[[] for _ in range(node+1)]
for _ in range(busNum):
        a,b,c = map(int, input().split())
        graph[a].append((c,b))

visited = [1e9] * (node +1)

def bfs(x):
    q = []
    heapq.heappush(q, (0,x)) # 왜 0,x인가 .........???????
    visited[x] = 0
    while q:
        cost, city = heapq.heappop(q)
        if visited[city] < cost:
            continue;
        for x, y in graph[city]:
            newCost = x+cost
            if(visited[y] > newCost ):
                visited[y] = newCost
                heapq.heappush(q, (newCost, y))


startCity, endCity = map(int, input().split())

bfs(startCity)
print(visited[endCity])