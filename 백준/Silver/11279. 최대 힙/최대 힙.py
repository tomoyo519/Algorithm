import sys
import heapq
input = sys.stdin.readline

num = int(input())
heap = []

for i in range(num):
    a = int(input())
    if a == 0:
        if heap:
            print((-1) * heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, (-1)*a)