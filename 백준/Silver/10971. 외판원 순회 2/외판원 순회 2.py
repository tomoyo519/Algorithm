import itertools
import math
city = int(input())
cityOptions = []
for i in range(0, city):
    cityOptions.append(i)
travel_cost = [list(map(int, input().split())) for _ in range(0,city)]

minNum = math.inf;

for option in itertools.permutations(cityOptions):
    cost = 0
    for o in range(0, len(option)-1):
        if(travel_cost[option[o]][option[o+1]]> 0):
            cost += travel_cost[option[o]][option[o+1]]
        else:
            cost = 0
            break;
    if(cost > 0 and travel_cost[option[-1]][option[0]] !=0 ):
        cost += travel_cost[option[-1]][option[0]]
    else:
        cost = 0;
    if(cost != 0):
        minNum = min(minNum, cost)    
    
print(minNum)