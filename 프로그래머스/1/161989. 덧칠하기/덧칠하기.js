function solution(n, m, sections) {
    var answer = 0; // 칠한 횟수
    var painted = 0; // 현재까지 색칠한 구간의 끝 위치
    for(var section of sections) {
        if(painted < section) { // 현재 구간이 아직 칠해지지 않은 경우,
            answer++;
            painted = section+m-1; // 색칠 후 끝 위치 업데이트
        }
    }
    return answer;
}