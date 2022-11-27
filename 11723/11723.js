const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
// 표준 입력으로 받아도 되고 mac 환경에선 input.txt로 받을 수 도 있게 해주는 코드
solution(input);

function solution(input) {
  let num = input[0] * 1;
  input.splice(0, 1);
  const set = new Set();
  for (let i = 0; i < num; i++) {
    const message = input[i].split(" ");

    if (message[0] === "add") set.add(message[1]);
    else if (message[0] === "check") {
      if (set.has(message[1])) console.log("1");
      else console.log("0");
    } else if (message[0] === "remove") set.delete(message[1]);
    else if (message[0] === "toggle") {
      if (set.has(message[1])) set.delete(message[1]);
      else set.add(message[1]);
    } else if (message[0] === "all") {
      for (let j = 1; j <= 20; j++) {
        set.add(j);
      }
    } else if (message[0] === "empty") set.clear();
    // console.log(set);
  }
}
