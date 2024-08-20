function solution(cards1, cards2, goal) {
    let i = 0; // cards1의 인덱스
    let j = 0; // cards2의 인덱스

    for (let word of goal) {
        if (i < cards1.length && cards1[i] === word) {
            i++;
        } else if (j < cards2.length && cards2[j] === word) {
            j++;
        } else {
            return "No"; // 만들어낼 수 없는 경우
        }
    }

    return "Yes"; // 목표를 달성한 경우
}