#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let char = c;
    if (!char) {
      char = 'X';
    }
    let string = '';
    for (let i = 0; i < this.width; i++) {
      string += char;
    }
    for (let i = 0; i < this.width; i++) {
      console.log(string);
    }
  }
};
