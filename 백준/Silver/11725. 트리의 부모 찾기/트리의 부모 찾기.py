import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
node = int(input())
graph= [[] for _ in range(node+1)]

for i in range(node -1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
parents= [ 0 for _ in range(node +1)]
parents[1] = 1
def dfs(start):
    for i in graph[start]:
        if parents[i] == 0: # 방문하지 않은 경우,
            parents[i] = start #부모를 설정준준다
            dfs(i)
dfs(1)   
for i in parents[2: ]:
    print(i)