function solution(array, commands) {
    let answer = [];
    for(let l=0; l<commands.length; l++){
        let [i,j,k] = commands[l];
        let newArr = array.slice(i-1, j).sort((a,b)=> a-b)
        console.log(newArr);
        answer.push(newArr[k-1])
    }
    return answer;
}