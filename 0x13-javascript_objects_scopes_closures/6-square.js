#!/usr/bin/node

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call the constructor of the base Square class
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X'; // Default character is 'X'
    }

    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
