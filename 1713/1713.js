const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
// 표준 입력으로 받아도 되고 mac 환경에선 input.txt로 받을 수 도 있게 해주는 코드
solution(input);

function solution(input) {
  const frame = input[0] * 1;
  const voteNum = input[1] * 1;
  const voteArr = input[2].split(" ");
  //   console.log(frame, voteNum, voteArr);

  const voteObj = new Object();

  voteArr.map((vote) => {
    if (voteObj[vote]) {
      voteObj[vote] += 1;
    } else {
      if (Object.keys(voteObj.length) > 3) voteObj[vote] = 1;
    }
  });
}
// 2 6 7
