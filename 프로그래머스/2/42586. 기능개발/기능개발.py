from collections import deque

def solution(progresses, speeds):
    answer = []
    # // 하루에 speed만큼 더해주고 백이면 count++ 해서 answer에 넣어주기,
    queue = deque(progresses)
    count = 0
    while progresses:
        if progresses[0] + speeds[0] >=100:
            progresses.pop(0)
            speeds.pop(0)
            count +=1
        else:
            if count !=0:
                answer.append(count)
                count = 0
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
    answer.append(count)
    print(answer)
    return answer