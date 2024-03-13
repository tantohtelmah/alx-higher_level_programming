#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  /**
     * Returns the number of occurrences of searchElement in the list.
     */
  return list.filter(item => item === searchElement).length;
};
