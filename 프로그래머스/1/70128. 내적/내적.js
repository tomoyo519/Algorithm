function solution(a, b) {
    let len = a.length;
    let answer = 0;
    for(let i=0; i<len; i++){
        answer += (a[i] * b[i])
    }
    return answer;
}