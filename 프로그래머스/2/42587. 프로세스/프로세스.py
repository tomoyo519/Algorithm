from collections import deque

def solution(priorities, location):
    process = deque()
    priorities = deque([(v, i) for i, v in enumerate(priorities)])
    while priorities:
        current = priorities[0]
        
        if any(current[0] < i[0] for i in priorities):
            priorities.rotate(-1)
        else:
            process.append(priorities.popleft())
    return [i[1] for i in process].index(location) + 1