#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // Create an empty object if w or h is not positive
      this.width = null;
      this.height = null;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width === null || this.height === null) {
      console.log(' ');
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;
