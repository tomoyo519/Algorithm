# 인저한 정점끼리 서로 다른색, 모든 정점은 두가지색으로 칠하기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

test = int(input())


def dfs(start):
    global result;
    for i in graph[start]:
        if(dfs_visited[i] == -1):
            if(dfs_visited[start] ==1):
                dfs_visited[i] =2
            if(dfs_visited[start]== 2):
                dfs_visited[i] =1
            dfs(i)
        else:
            if(dfs_visited[start] == dfs_visited[i]):
                result = False
                return;
                
for _ in range(test):
    node, line = map(int, input().split())
    dfs_visited = [-1] * (node +1)
    graph = [[] for _ in range(node+1)]
    
    for _ in range(line):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = True
    
    for i in range(1, node+1): # 모든 노드 탐색
        if(dfs_visited[i] == -1): # 현재 노드가 색칠되어있지 않다면
            dfs_visited[i] =1; #현재 노드를 색칠
            dfs(i) #이웃한 노드에 대해서 색칠
            if(result == False): #이분 그래프가 아니다.
                    break;
                    
    if(result == False):
        print("NO")
    else:
        print("YES")