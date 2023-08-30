import sys
input = sys.stdin.readline
# 선택하지 않았을 때 더 최적인 경우 ???????
import heapq

N = int(input())
arr = [ list(map(int, input().rstrip().split())) for _ in range(N)]
arr.sort(key=lambda x:x[0])

q = []

for time, cup in arr:

    heapq.heappush(q, cup) #컵라면 갯수 를 큐에 넣기
    if (time <len(q)):
        heapq.heappop(q) #가장 작은 컵라면 개수를 빼준다
        
print(sum(q))