def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        temp = array[i-1: j]
        temp.sort()
        answer.append(temp[k-1])
    return answer