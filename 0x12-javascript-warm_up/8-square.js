#!/usr/bin/node
const process = require('process');
const args = process.argv;
const iter = parseInt(args[2]);
const char = 'X';
let string = '';
if (!iter) {
  console.log('Missing size');
}
for (let i = 0; i < iter; i++) {
  string += char;
}
for (let i = 0; i < iter; i++) {
  console.log(string);
}
