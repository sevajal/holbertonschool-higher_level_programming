#!/usr/bin/node
exports.addMeMaybe = function (number, addMeMaybe) {
  number++;
  addMeMaybe(number);
};
