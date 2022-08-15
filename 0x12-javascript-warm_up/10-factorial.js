#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
const process = require('process');
const args = process.argv;
let myNumber = Number(args[2]);
if (!myNumber) {
  myNumber = 1;
}
console.log(factorial(myNumber));
