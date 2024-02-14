#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0) {
            // Create an empty object (initialize attributes to undefined)
            this.width = undefined;
            this.height = undefined;
        } else {
            this.width = w;
            this.height = h;
        }
    }

    print() {
        if (this.width === undefined || this.height === undefined) {
            console.log("Empty rectangle");
        } else {
            for (let i = 0; i < this.height; i++) {
                console.log("X".repeat(this.width));
            }
        }
    }

    rotate() {
        if (this.width !== undefined && this.height !== undefined) {
            [this.width, this.height] = [this.height, this.width];
        }
    }

    double() {
        if (this.width !== undefined && this.height !== undefined) {
            this.width *= 2;
            this.height *= 2;
        }
    }
}
module.exports = Rectangle;

