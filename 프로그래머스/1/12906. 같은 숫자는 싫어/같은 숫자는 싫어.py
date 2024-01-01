import sys
input = sys.stdin.readline
def solution(arr):

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    curr = arr[0]
    result = []
    result.append(curr)
    for i in range(1, len(arr)):

        if arr[i] == curr:
            continue;
        else:
            curr = arr[i]
            result.append(arr[i])
    return result            