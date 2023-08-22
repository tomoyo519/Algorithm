import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
number = int(input())
insideout = list(map(str,input().strip()))
insideout.insert(0,'0') #[0.1.0.1.1.1]

graph = [[] for _ in range(number+1)]
for _ in range(number-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0;

def dfs(start):
    global count, dfs_visited
    dfs_visited[start] = True
    for i in graph[start]: #[2]

        if not dfs_visited[i] :
            if(insideout[i] == "1"):
              
                dfs_visited[i] = True
                count+=1;
                # return ???
            else:
                dfs_visited[i] = True
                dfs(i)

for j in range(1, number+1): # 조건 이거 맞음?
    dfs_visited = [False] * (number + 1)
    if(insideout[j] == '1'):
        dfs(j)
        
print(count)