import sys
from collections import deque
input = sys.stdin.readline

node, line, start = map(int,input().split())

graph = [ [] for _ in range(node+1)]

for i in range(line):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for j in graph: 
    j.sort()

dfs_visited=[False] * (node +1)
def dfs(start):
    dfs_visited[start] = True
    print(start, end= " ");
    for i in graph[start]:
        if not dfs_visited[i]:
            dfs(i)
            
bfs_visited=[False] * (node + 1)
def bfs(start):
    queue = deque([start])
    bfs_visited[start] = True;
    while(queue):
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not bfs_visited[i]:
                bfs_visited[i]= True
                queue.append(i)
dfs(start)
print()
bfs(start)