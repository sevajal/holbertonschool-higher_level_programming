#!/usr/bin/node
const logList = [];
let index = 0;
exports.logMe = function (item) {
  logList.push(item);
  console.log(`${index}: ${logList[index]}`);
  index++;
};
