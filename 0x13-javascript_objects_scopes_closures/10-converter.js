#!/usr/bin/node
exports.converter = function (base) {
  return myConvert => myConvert.toString(base);
};
