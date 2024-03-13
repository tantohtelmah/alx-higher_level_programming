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
      console.log('Empty rectangle');
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate () {
    if (this.width !== null && this.height !== null) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double () {
    if (this.width !== null && this.height !== null) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
