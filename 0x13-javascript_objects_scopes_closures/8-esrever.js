#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  const length = list.length;
  for (let i = 0; i < length; i++) {
    newList.push(list.pop());
  }
  return (newList);
};
