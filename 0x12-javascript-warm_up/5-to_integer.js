#!/usr/bin/node

// Get the first argument from the command-line
const firstArgument = process.argv[2];

// Convert the argument to an integer
const parsedNumber = parseInt(firstArgument, 10);

// Check if the conversion was successful
if (!isNaN(parsedNumber)) {
  console.log(`My number: ${parsedNumber}`);
} else {
  console.log('Not a number');
}
