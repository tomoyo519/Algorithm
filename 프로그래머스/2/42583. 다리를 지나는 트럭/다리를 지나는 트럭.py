from collections import deque
def solution(bridge_length, weight, truck_weights):
    tick = 0
    ing = deque( [0] * bridge_length);
    sum_num = 0
    while ing:
        sum_num -=ing.popleft()
        tick +=1
        if truck_weights:
            if sum_num + truck_weights[0] <= weight:
                sum_num += truck_weights[0]
                now = truck_weights.pop(0)
                ing.append(now)
            else:

                ing.append(0)

    return tick
    