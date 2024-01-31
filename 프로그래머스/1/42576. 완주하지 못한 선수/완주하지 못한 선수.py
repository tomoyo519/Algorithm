def solution(participant, completion):
    p = sorted(participant)
    c = sorted(completion)
    for i in range(len(c)):
        if p[i] != c[i]:
            return p[i]

    return p[-1]
    