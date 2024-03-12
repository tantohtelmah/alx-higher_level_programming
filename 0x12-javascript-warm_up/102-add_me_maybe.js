#!/usr/bin/node

exports.addMeMaybe = function incrementAndCall(number, theFunction) {
  const incrementedNumber = number + 1;
  theFunction(incrementedNumber);
}
