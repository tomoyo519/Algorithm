function solution(arr) {
    let answer = [];
    let minNum = Number.MAX_SAFE_INTEGER;
    for(let i=0; i<arr.length; i++){
        if (arr[i] < minNum) minNum = arr[i]
    }
    console.log(minNum)
    const result = arr.filter((el)=> el !== minNum)
    return result === [] ? [-1]: result;
}