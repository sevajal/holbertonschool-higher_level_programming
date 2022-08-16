#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
const data1 = fs.readFileSync(args[2], 'utf8');
const data2 = fs.readFileSync(args[3], 'utf8');
const fullData = data1.concat(data2);
fs.writeFile(args[4], fullData, err => {
  if (err) {
    console.error(err);
  }
});
