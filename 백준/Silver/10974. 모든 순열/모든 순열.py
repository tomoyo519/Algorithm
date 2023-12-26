import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input());
nums = []
for i in range(1, n+1):
    nums.append(i)
    
permutaions_list = list(permutations(nums))

for permutation in permutaions_list:
    print(' '.join(map(str, permutation)))