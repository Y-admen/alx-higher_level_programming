#!/usr/bin/node
const args = process.argv.slice(1);
if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
