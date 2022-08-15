#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
}
if (args.length > 3) {
  args.splice(0, 2);
  args.sort();
  args.reverse();
  console.log(args[1]);
}
