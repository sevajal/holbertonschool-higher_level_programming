#!/usr/bin/node
exports.callMeMoby = function (x, callMeMoby) {
  const args = process.argv;
  for (let i = 0; i < x; i++) {
    callMeMoby(args[2]);
  }
};
