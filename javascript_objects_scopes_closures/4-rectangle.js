#!/usr/bin/node
class Rectangle {
  // initialization method
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  // print method to print a rectangle
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // rotate method that switches width and height
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // double method that multiples w + h by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
