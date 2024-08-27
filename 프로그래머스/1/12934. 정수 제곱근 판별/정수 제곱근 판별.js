function solution(n) {
    let sqrt = Math.sqrt(n)
    return Number.isInteger(sqrt) ? (sqrt+1)*(sqrt+1) : -1
}