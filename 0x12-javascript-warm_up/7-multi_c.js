#!/usr/bin/node
const process = require('process');
const args = process.argv;
const iter = parseInt(args[2]);
const string = 'C is fun';
if (iter) {
  for (let i = 0; i < iter; i++) {
    console.log(string);
  }
} else {
  console.log('Missing number of occurrences');
}
