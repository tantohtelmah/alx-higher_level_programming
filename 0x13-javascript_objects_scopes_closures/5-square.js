#!/usr/bin/node

// ChildClass.js
import { Rectangle } from '4-rectangle.js';

class Square extends Rectangle {
    constructor(size) {
        super(size, size); // Call the parent class constructor
	}
}
module.exports = Square;
