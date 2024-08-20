function solution(s) {
    const result = Array(s.length).fill(-1); // 결과 배열 초기화
    const lastIndexMap = {}; // 마지막 인덱스를 저장할 객체

    for (let i = 0; i < s.length; i++) {
        const char = s[i]; // 현재 문자
        if (lastIndexMap[char] !== undefined) {
            result[i] = i - lastIndexMap[char]; // 마지막 인덱스와의 차이 계산
        }
        lastIndexMap[char] = i; // 현재 문자의 인덱스 저장
    }

    return result;
}

