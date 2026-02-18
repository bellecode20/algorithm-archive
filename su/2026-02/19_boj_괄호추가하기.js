// 괄호 추가하기 https://www.acmicpc.net/problem/16637
const fs = require('fs');
// 로컬 테스트용: input.txt, 백준 제출용: /dev/stdin
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');

// 1. 입력 처리
const N = Number(input[0]);
const expression = input[1].trim();

// 2. 숫자와 연산자 분리
const numbers = [];
const operators = [];

// expression을 순회하며 분리 (파이썬의 enumerate 대신 일반 for문 사용)
for (let i = 0; i < N; i++) {
  const ch = expression[i];
  if (i % 2 === 0) {
    numbers.push(Number(ch)); // 숫자로 변환해서 저장
  } else {
    operators.push(ch);
  }
}

// 3. 정답 변수 초기화 (매우 작은 수로 설정)
// 자바스크립트에서 -1e9도 되지만, -Infinity가 더 안전합니다.
let answer = -Infinity;

// 4. 계산 함수 (cal)
const cal = (a, op, b) => {
  if (op === '+') return a + b;
  if (op === '-') return a - b;
  if (op === '*') return a * b;
  return 0;
};

// 5. DFS 함수
const dfs = (idx, curVal) => {
  if (idx === operators.length) {
    answer = Math.max(answer, curVal);
    return;
  }

  const noBracketVal = cal(curVal, operators[idx], numbers[idx + 1]);
  dfs(idx + 1, noBracketVal);

  if (idx + 1 < operators.length) {
    const bracketVal = cal(numbers[idx + 1], operators[idx + 1], numbers[idx + 2]);
    const withBracketVal = cal(curVal, operators[idx], bracketVal);
    
    // 연산자 2개를 썼으므로 idx + 2로 점프
    dfs(idx + 2, withBracketVal);
  }
};

// 6. 실행 및 출력
// 첫 번째 숫자를 초기값으로 넣고 시작
dfs(0, numbers[0]);

console.log(answer);
