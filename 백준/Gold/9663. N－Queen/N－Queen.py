import sys
def is_available(candidate, current_col):
	current_row = len(candidate)
	for queen_row in range(current_row):
		if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
				return False
	return True

def solve_n_quue(N):
	final_result = []
	#current_candidate = 현재 퀸의 위치(이미 배치된것)
	DFS(N, 0, [], final_result)
	print(len(final_result))
    
def DFS(N,current_row, current_candidate,final_result):
	if current_row == N:
		final_result.append(current_candidate[:])
		return
	else:
		for candidate_col in range(N):
			if is_available(current_candidate, candidate_col): # pluning
				current_candidate.append(candidate_col)
				DFS(N, current_row + 1, current_candidate, final_result)
				current_candidate.pop() # 백트래킹 하는 부분
    
number = int(sys.stdin.readline())
solve_n_quue(number)