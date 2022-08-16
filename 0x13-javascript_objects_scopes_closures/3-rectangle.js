#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const char = 'X';
    let string = '';
    for (let i = 0; i < this.width; i++) {
      string += char;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(string);
    }
  }
};
