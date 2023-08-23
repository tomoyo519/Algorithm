import sys
input = sys.stdin.readline
from collections import deque;

width, height = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(height)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q= deque([])

# 처음 익은 토마토의 위치를 queue 에 넣어줘야 함.
for i in range(height):
    for j in range(width):
        if(graph[i][j]==1):
            q.append([i,j])
    

result = 0;
def bfs():
    while q:
            nowx, nowy = q.popleft()
            for i in range(4):
                newX = nowx + dx[i]
                newY = nowy + dy[i]

                if(0<=newX<height and 0<=newY < width and graph[newX][newY] == 0): # 범위를 넘지 않고, 다음 토마토가 익지 않은 채라면,
                    graph[newX][newY] = graph[nowx][nowy]+1;
                    q.append([newX, newY])
                

bfs()
for i in graph:
    for j in i:
        if j ==0:
            print(-1)
            exit(0)
    result = max(result,max(i))
    
print(result -1)
                