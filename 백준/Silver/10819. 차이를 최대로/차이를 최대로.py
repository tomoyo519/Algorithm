import itertools
number = int(input());
arr = list(input().split())
options = list(itertools.permutations(arr))
solution = []
for i in range(0, len(options)):
    result = 0;
    for k in range(1, len(arr) ):
        result+= abs(int(options[i][k-1]) - int(options[i][k]))
    solution.append(result)

print(max(solution))