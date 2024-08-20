function solution(numbers) {
    var answer = 0;
    let sum = 0;
    for(let i = 0; i < 10; i++){
      sum += i; // 변수 sum에 모든 항의 값 더하기
    }
    for(let j = 0; j < numbers.length; j++){
      
      sum -= numbers[j]; // 없는 숫자의 합을 더하는 거니까 sum에서 있는 숫자를 모두 뺌
    }
    answer = sum;
    return answer;
}