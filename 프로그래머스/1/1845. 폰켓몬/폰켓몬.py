def solution(nums):
    max = len(nums) // 2 # 3
    length = len(set(nums)) # 2
    if max <= length:
        return max
    return length