function solution(arr) {
    const initialValue = 0;
const sumWithInitial = arr.reduce(
  (acc, cur) => acc + cur,
  initialValue,
);
    return sumWithInitial / arr.length 
}