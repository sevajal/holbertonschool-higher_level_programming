#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
}
if (args.length > 3) {
  args.splice(0, 2);
  const newArgs = args.map(Number);
  newArgs.sort(function (a, b) { return b - a; });
  console.log(newArgs[1]);
}
