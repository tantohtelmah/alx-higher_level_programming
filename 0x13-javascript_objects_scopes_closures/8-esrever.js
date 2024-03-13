#!/usr/bin/node

exports.esrever = function (list) {
  /**
     * Returns the reversed version of the list.
     */
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
