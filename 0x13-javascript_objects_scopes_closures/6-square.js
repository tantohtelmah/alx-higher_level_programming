#!/usr/bin/node

class Square extends Square {
    constructor(size) {
        super(size);
    }

    charPrint(c) {
        if (!c) {
            c = 'X';
        }
        for (let i = 0; i < this.size; i++) {
            console.log(c.repeat(this.size));
        }
    }
}
module.exports = Square;
