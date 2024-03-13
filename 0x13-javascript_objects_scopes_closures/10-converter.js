#!/usr/bin/node

exports.converter = function (base) {
  /**
     * Converts a number from base 10 to the specified base.
     */
  return function (number) {
    if (number === 0) {
      return '0'; // Special case for zero
    }

    let result = '';
    while (number > 0) {
      const digit = number % base;
      result = digit + result;
      number = Math.floor(number / base);
    }

    return result;
  };
};
