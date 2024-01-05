def solution(numbers, target):
    answer = 0
    
    def calc(idx, sum):
        nonlocal answer
        if idx == len(numbers):
            if target == sum:
                answer+=1
            return
        
        calc(idx +1 , sum + numbers[idx])
        calc(idx+1, sum - numbers[idx])
    calc(0,0)
    return answer