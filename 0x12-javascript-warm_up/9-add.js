#!/usr/bin/node
const args = process.argv.slice(2);

function add (a, b) {
  return a + b;
}

const num1 = parseInt(args[0]);
const num2 = parseInt(args[1]);

if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
