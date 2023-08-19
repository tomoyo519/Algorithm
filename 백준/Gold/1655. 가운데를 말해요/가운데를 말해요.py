import sys
import heapq
input = sys.stdin.readline  

#left 는 최대힙으로, right 는 최소힙으로 구성함으로써 leftheap 의 첫원소를 중간값으로
number = int(input())
leftheap = []
rightheap = []
for i in range(number):
    command = int(input())
    if(len(leftheap) == len(rightheap)):
        heapq.heappush(leftheap, -command)
    else:
        heapq.heappush(rightheap, command)
        
    if rightheap and -leftheap[0] > rightheap[0]:
        leftValue = heapq.heappop(leftheap)
        rightValue = heapq.heappop(rightheap)
        heapq.heappush(leftheap, -rightValue)
        heapq.heappush(rightheap, -leftValue)
    print(-leftheap[0])
