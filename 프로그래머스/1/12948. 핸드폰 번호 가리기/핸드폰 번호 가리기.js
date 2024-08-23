function solution(phone_number) {
    let answer = '';
    let lastFourDigits = phone_number.slice(-4)
    for(let i=0; i<phone_number.split('').length -4;i++){
        answer += '*'
    }
    return answer+lastFourDigits;
}