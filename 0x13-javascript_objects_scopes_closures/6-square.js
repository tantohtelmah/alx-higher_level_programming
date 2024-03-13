#!/usr/bin/node

const BaseSquare = require('./5-square');
class Square extends BaseSquare {
  constructor (size) {
    super(size); // Call the constructor of the base Square class
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
