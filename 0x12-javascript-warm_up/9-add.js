#!/usr/bin/node
const args = process.argv.slice(2);
const int1 = parseInt(args[0], 10);
const int2 = parseInt(args[1], 10);

function add (int1, int2) {
  console.log(int1 + int2);
}

add(int1, int2);
