from collections import deque

def solution(maps):

    n,m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    dx = [-1, 1, 0 , 0]
    dy = [0, 0, -1, 1]
    queue = deque([(0,0)]);
    visited[0][0] = True
        
    while queue:
        x, y = queue.popleft();
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] +1
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
    
    
