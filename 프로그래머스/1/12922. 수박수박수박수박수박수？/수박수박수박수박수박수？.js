function solution(n) {
  let answer = '';
  if (n % 2 === 0){ // n = 짝수인경우,
    answer = '수박'.repeat(n/2)
  }else { // n = 홀수인경우,
    answer = '수박'.repeat((n-1)/2) + '수'
  }
  return answer;
}