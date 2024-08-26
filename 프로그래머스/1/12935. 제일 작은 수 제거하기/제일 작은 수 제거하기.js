function solution(arr) {
    if(arr.length ===1) return [-1]
    let minNum = Math.min(...arr)
    let newArr = arr.filter((digit) => digit !== minNum)
    return newArr;
}