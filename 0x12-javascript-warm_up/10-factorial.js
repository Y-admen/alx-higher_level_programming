#!/usr/bin/node
const args = process.argv.slice(2);
const num = parseInt(args[0], 10);
if (isNaN(num)) {
  console.log('1');
} else {
  let fac = 1;
  for (let i = num; i >= 1; i -= 1) {
    fac *= i;
  }
  console.log(fac);
}
