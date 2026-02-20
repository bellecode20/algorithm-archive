// 괄호 추가하기 https://www.acmicpc.net/problem/16637

const fs = require('fs');
// 로컬 테스트용: input.txt, 백준 제출용: /dev/stdin
const filePath = process.platform === 'linux' ? '/dev/stdin' : '../input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

// slice, 
// 배열.join(" ")
// 배열.length
// 

const solve = (numbers, k, N) => {

  const dfs = (start, history) => {
    if (history.length === 6) {
      console.log(history.join(" "))
      return
    }
  
    for(let i = start; i < N; i++){

      history.push(numbers[i])
      dfs(i + 1, history)
      history.pop()
    }
  
  };
  
  dfs(0, [])
  console.log()
}



let index = 0;
while (true){
  const arr = input[index++].split(" ").map(Number);
  const k = arr[0];
  
  if (k === 0) {
    break;
  }
  
  const numbers = arr.slice(1);  // 1번째값부터 배열 잘라오기 (시작인덱스포함, 끝인덱스미포함)
  const N = numbers.length;

  solve(numbers, k, N)

}


  