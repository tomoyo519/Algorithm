import sys
input = sys.stdin.readline
from collections import deque


node = int(input())
line = int(input())

graph = [[] for _ in range(node+1)]
for _ in range(line):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
count = 0;
dfs_visited = [False] * ( node + 1 )
def dfs(start):
    global count
    dfs_visited[start] = True;
    for i in graph[start]:
        if not dfs_visited[i]:
            count += 1
            dfs(i)
dfs(1)
print(count)