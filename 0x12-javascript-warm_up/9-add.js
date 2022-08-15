#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const process = require('process');
const args = process.argv;
add(Number(args[2]), Number(args[3]));
