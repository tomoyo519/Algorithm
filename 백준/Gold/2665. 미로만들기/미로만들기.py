import sys
input = sys.stdin.readline
import heapq

num = int(input())
graph = []
for i in range(num):
    graph.append(list(map(int, input().rstrip())))
    
dx = [ -1, 1, 0, 0]
dy = [0, 0, -1 ,1]

visited = [[False] * (num) for _ in range(num)]


def bfs(x,y):
    queue = []
    heapq.heappush(queue, (0, x,y))
    while(queue):
        count, nowx, nowy = heapq.heappop(queue)
        visited[nowx][nowy] = True

        if nowx == (num -1) and nowy == (num-1):
            return count;
        for j in range(4):
            nx = nowx+ dx[j]
            ny = nowy+ dy[j]
            if( 0<=nx<num and 0<=ny<num and not visited[nx][ny]):
                visited[nx][ny] = True;
                if(graph[nx][ny] == 1): #흰방인 경우,
                    heapq.heappush(queue,(count, nx,ny))
                else:
                    heapq.heappush(queue, (count+1, nx, ny))

print(bfs(0,0))

