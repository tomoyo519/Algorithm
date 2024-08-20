function solution(n) {
    let arr = Array(n + 1).fill(true)
    arr[0] = false
    arr[1] = false
// n까지의 배수를 모두 false 처리하는 방법ㄷ
 // 제곱근까지만 반복
    for(let i = 2; i * i <= n; i++) {
        if(arr[i]) {
            for(let j = i * i; j <= n; j += i) {
                // 배수라면 소수가 아님 => false
                                arr[j] = false 
            }
        }
    }

    return arr.filter(el => el).length
}