function solution(number, limit, power) {
    let total = 0;

    for (let i = 1; i <= number; i++) {
        let count = 0;

        // 약수의 개수 계산
        for (let j = 1; j * j <= i; j++) {
            if (i % j === 0) {
                count++; // j는 약수
                if (j !== i / j) count++; // i/j도 약수 (다를 경우)
            }
        }

        // 약수의 개수에 따라 total에 추가
        if (count > limit) {
            total += power;
        } else {
            total += count;
        }
    }

    return total;
}
