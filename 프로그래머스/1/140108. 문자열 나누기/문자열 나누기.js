function solution(s) {
    let answer = 0;
    let countX = 0;
    let countOther = 0;
    let x = '';

    for (let char of s) {
        if (countX === 0) {
            x = char;  // 첫 문자 설정
        }
        if (char === x) {
            countX++;  // x의 개수 증가
        } else {
            countOther++;  // 다른 문자의 개수 증가
        }

        if (countX === countOther) {
            answer++;  // 분리 가능할 때마다 증가
            countX = 0;  // 카운터 초기화
            countOther = 0; 
        }
    }

    // 마지막에 남은 문자열이 있으면 추가
    if (countX > 0 || countOther > 0) {
        answer++;
    }

    return answer;
}

// 예제 실행

