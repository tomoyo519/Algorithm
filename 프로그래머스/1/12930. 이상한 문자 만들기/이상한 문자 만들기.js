function solution(s) {
    let answer = []; 
    let arr = s.split(' ')
    for(let i=0; i<arr.length; i++){
        let word = arr[i].split(''); // try
        let newWord = '';
        for(let j=0; j<word.length; j++){ // ['t','r','y']     
            if(j % 2 === 0 ){
                newWord += word[j].toUpperCase();
            }else if(j % 2 === 1){
               newWord += word[j].toLowerCase();
            } 
}
        answer.push(newWord)
    }
    return answer.join(' ')
}