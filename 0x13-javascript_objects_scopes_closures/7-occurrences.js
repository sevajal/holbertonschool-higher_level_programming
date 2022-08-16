#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurances = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occurances++;
    }
  }
  return (occurances);
};
