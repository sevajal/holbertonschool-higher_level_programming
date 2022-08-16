#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const [k, v] of Object.entries(dict)) {
  if (!newDict[v]) {
    newDict[v] = [];
  }
  newDict[v].push(k);
}
console.log(newDict);
