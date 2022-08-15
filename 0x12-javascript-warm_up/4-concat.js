#!/usr/bin/node
const process = require('process');
const args = process.argv;
const stringConcat = args[2] + ' is ' + args[3];

console.log(stringConcat);
