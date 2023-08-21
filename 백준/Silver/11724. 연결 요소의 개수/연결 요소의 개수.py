import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
node, line = map(int, input().split())
graph = [[] for _ in range(node+1)]
for _ in range(line):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs_visited = [False] * (node + 1)
# def dfs(start):
#     dfs_visited[start] = True;
#     for i in graph[start]:
#         if not dfs_visited[i]:
#             dfs(i)
            
# count = 0
# for i in range(1, node+1):
#     if not dfs_visited[i]:
#         dfs(i)
#         count+=1
# print(count)

bfs_visited = [False] * (node+1)
def bfs(start):
    queue = deque([start])
    bfs_visited[start] = True;
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not bfs_visited[i]:
                
                bfs_visited[i] = True;
                queue.append(i);
                
count = 0;
for i in range(1, node+1):
    if not bfs_visited[i]:

        bfs(i)
        count += 1;
print(count)