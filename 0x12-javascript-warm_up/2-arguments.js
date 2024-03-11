#!/usr/bin/node

// number of command-line arguments
const numArguments = process.argv.length - 2;
// Check the number of arguments and print the appropriate message
if (numArguments === 0) {
  console.log('No argument');
} else if (numArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
