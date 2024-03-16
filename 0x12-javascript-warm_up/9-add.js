#!/usr/bin/node
const arg = Math.floor(Number(process.argv[2]));
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

function add (a, b) {
  return (a + b);
}
if (isNaN(arg)) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}
