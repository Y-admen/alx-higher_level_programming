#!/usr/bin/node
const args = process.argv.slice(2);
const num = parseInt(args[0], 10);
let str = '';
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i += 1) {
    for (let i = 0; i < num; i += 1) {
      str += 'X';
    }
    console.log(str);
    str = '';
  }
}
