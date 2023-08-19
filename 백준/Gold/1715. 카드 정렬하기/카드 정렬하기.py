import sys
import heapq
input = sys.stdin.readline

number = int(input())
result = []

for i in range(number):
    command = int(input())
    heapq.heappush(result, command)
    
dap = 0

if(len(result)==1):
    print(dap)
else:
    
    for j in range(number -1):
        smallest = heapq.heappop(result)
        secSmallest = heapq.heappop(result)
        dap += smallest + secSmallest
        heapq.heappush(result, (smallest + secSmallest))
    print(dap)
    


