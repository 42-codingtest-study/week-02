const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
// 표준 입력으로 받아도 되고 mac 환경에선 input.txt로 받을 수 도 있게 해주는 코드
solution(input);

function solution(input) {
  let n = input[0] * 1;
  const arr = new Array(n).fill(0).map(() => new Array(n).fill(0));
  const dx = [1, 0, -1, 0];
  const dy = [0, 1, 0, -1]; // 아래 오른쪽 위 왼쪽
  let num = n * n;
  let x = 0; // x 좌표
  let y = 0; // y 좌표
  let i = 0;
  let bool = true;
  let nx = x;
  let ny = y;
  let second_answer = { x: 0, y: 0 };
  while (bool) {
    if (num === input[1] * 1) {
      second_answer.x = x + 1;
      second_answer.y = y + 1;
    }
    arr[x][y] = num;
    nx = x + dx[i];
    ny = y + dy[i];
    // console.log(nx, ny, i);
    if (nx >= n || ny >= n || nx <= -1 || ny <= -1 || arr[nx][ny] !== 0) {
      i += 1;
      if (i === 4) i = 0;
      continue;
    }
    x = nx;
    y = ny;
    num -= 1;
    if (num === 1) {
      bool = false;
    }
  }
  arr[x][y] = 1;
  for (let i = 0; i < arr.length; i++) {
    console.log(arr[i].join(" "));
  }
  if (input[1] * 1 === 1) {
    console.log(`${(input[0] * 1 + 1) / 2} ${(input[0] * 1 + 1) / 2}`);
  } else {
    console.log(`${second_answer.x} ${second_answer.y}`);
  }
}
