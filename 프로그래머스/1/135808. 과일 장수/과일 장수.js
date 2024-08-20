function solution(k, m, score) {
    // 가격 배열을 오름차순으로 정렬
    score.sort((a, b) => a - b);
    
    let totalProfit = 0;
    const n = score.length;

    // m개씩 묶어서 계산
    for (let i = n - m; i >= 0; i -= m) {
        totalProfit += score[i] * m; // 가장 비싼 과일의 가격을 더함
    }

    return totalProfit;
}
