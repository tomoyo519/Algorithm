function solution(ingredient) {
    let answer = 0;
    const stack = [];

    for(let i of ingredient) {
    	// stack에 ingredient 요소 추가
        stack.push(i);
        
        if(canMakeBugger(stack)) {
            answer++;
            // 햄버거를 구성한 재료 제거
            stack.length -= 4;
        }
    }
    return answer;
}

// stack 내 최근 4개의 요소로 햄버거를 만들 수 있는지 검사
function canMakeBugger(arr) {
    const [isFirstOne, isTwo, isThree, isSecondOne] = arr.slice(arr.length-4);
    return (isFirstOne === 1
        && isTwo === 2
        && isThree === 3
        && isSecondOne === 1);
}