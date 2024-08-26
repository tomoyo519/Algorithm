const fs = require('fs');
const input = fs.readFileSync('dev/stdin').toString().trim().split('\n');

/**
	1. 보드의 각 조각을 이중배열로 치환
    2. 보드에서 체스판을 만들기 위한 시작점 범위
    3. 두 가지 패턴과 다시 칠해야하는 조각
    4. 모든 시작점을 기점으로 8 * 8 크기로 보드를 자름
    5. 8 * 8 크기로 자른 범위에서 첫 조각의 패턴 인식 : 'B' 인경우, 'W'인 경우
    6. 8 * 8 범위의 각 조각들을 모두 조회하여 패턴과 비교
    7. 다음 줄 첫 조각의 체스판 패턴
    8. 해당 8 * 8 보드에서 다시 칠해야하는 조각 갯수를 result에 삽입
    9. result에서 최소값 출력

*/

const [M, N] = input[0].split(' ')
const bord = input.filter((cur,idx)=> idx != 0).map(el=>el.split('')) // 1.

let [y, x] = [M-8, N-8] // 2.
const arr = []; 
for(let yy = 0 ; yy <= y ; yy++){
  for(let xx = 0 ; xx <= x ; xx++){
    arr.push([yy,xx])
  }
}

// 3.
let pattern;
let pattern2;
let count = 0;
let count2 = 0;
let result = [];

// 4.
for([startY,startX] of arr){
  
  //5.
  pattern = bord[startY][startX]
  pattern2 = bord[startY][startX] === 'B' ? 'W' : 'B';

  //6.
  for(let i = startY ; i < startY+8 ; i++){
    for(let j = startX ; j < startX+8 ; j++){

      if(pattern !== bord[i][j]) count++;
      if(pattern2 !== bord[i][j]) count2++;

      pattern === 'B' ? (pattern = 'W') : ( pattern = 'B');
      pattern2 === 'B' ? (pattern2 = 'W') : ( pattern2 = 'B');
    }
    // 7.
    pattern === 'B' ? (pattern = 'W') : ( pattern = 'B');
    pattern2 === 'B' ? (pattern2 = 'W') : ( pattern2 = 'B');

  }
  // 8.
  result.push(count);
  result.push(count2);
  count2=0;
  count = 0;
}

// 9.
console.log(Math.min(...result))