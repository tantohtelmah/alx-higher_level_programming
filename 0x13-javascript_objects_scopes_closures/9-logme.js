#!/usr/bin/node

exports.logMe = function (item, count = [0]) {
  /**
     * Prints the number of arguments already printed and the new argument value.
     */
  console.log(`${count[0]}: ${item}`);
  count[0] += 1;
};
