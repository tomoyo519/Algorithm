import sys
input = sys.stdin.readline
from collections import deque
width, height = map(int, input().split())

maze = []
for i in range(width):
    tmp = list(map(int, input().rstrip()))
    maze.append(tmp)
    


# 상하좌우
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while(queue):
        x, y= queue.popleft()
        for i in range(4): # 0, 1, 2, 3
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<width and 0<=ny<height and maze[nx][ny] ==1):
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] +1


    return maze[width-1][height-1]

print(bfs(0,0))