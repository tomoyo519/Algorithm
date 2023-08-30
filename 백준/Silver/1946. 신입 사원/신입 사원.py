import sys
input = sys.stdin.readline

test = int(input())

for _ in range(test):
    N = int(input())
    count = 1;
    
    workers = [ list(map(int, input().split())) for _ in range(N)]

    workers.sort()
    min_workers = workers[0][1]
    
    for i in range(1,N):
        if workers[i][1] < min_workers:
            count +=1;
            min_workers = workers[i][1]
    print(count)
        