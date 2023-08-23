import sys
from collections import deque;
input = sys.stdin.readline

x,y,z = map(int, input().split())
move = [(0,0,1), (0,1,0), (1,0,0), (0,0,-1), (0,-1, 0), (-1, 0,0)]
graph = [ [list(map(int, input().split())) for _ in range(y) ] for _ in range(z)]
q = deque()

for i in range(z):
    for j in range(y):
        for k in range(x):
            if(graph[i][j][k] ==1):
                q.append([i,j,k])
                

def bfs():
    while q:
        nowx, nowy, nowz = q.popleft()
        for i in range(6):
            newx = nowx + move[i][0]
            newy = nowy + move[i][1]
            newz = nowz + move[i][2]
            
            if(0<=newx<z and 0<=newy<y and 0<=newz<x and graph[newx][newy][newz] == 0):
                graph[newx][newy][newz] = graph[nowx][nowy][nowz] +1
                q.append([newx,newy,newz])
                
                
bfs()
res = 0
for i in range(z):
    for j in range(y):
        for k in range(x):
            if(graph[i][j][k] == 0):
                print(-1)
                exit(0)
            res = max(res,graph[i][j][k])
print(res -1)