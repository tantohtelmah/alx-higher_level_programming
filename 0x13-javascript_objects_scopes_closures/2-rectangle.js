#!/usr/bin/node

// checks is weight and height are positive and not zero
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
}
