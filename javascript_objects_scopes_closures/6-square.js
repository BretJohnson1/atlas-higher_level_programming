#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  // initialization method
  constructor (size) {
    super(size, size);
  }

  // print method that changes char printed from x to c
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
