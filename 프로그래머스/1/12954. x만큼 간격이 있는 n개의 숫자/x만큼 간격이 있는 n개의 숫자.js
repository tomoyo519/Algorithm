function solution(x, n) {
    let answers = []
    let firstNum = 0;
    for(let i=1; i<=n;i++){
        firstNum+=(x)
        answers.push(firstNum)
    }
    return answers
}