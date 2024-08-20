function solution(t, p) {
    const tLength = t.length;
    const pLength = p.length;
    let count = 0;

    for (let i = 0; i <= tLength - pLength; i++) {
        const substring = t.substring(i, i + pLength); // t의 부분 문자열 추출
        if (substring <= p) {
            count++;
        }
    }

    return count;
}