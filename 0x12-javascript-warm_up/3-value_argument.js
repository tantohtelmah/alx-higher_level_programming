#!/usr/bin/node

// Gets the first argument (index 2) from the command-line arguments
const firstArgument = process.argv[2];

// Check if an argument was provided
if (firstArgument) {
  console.log(firstArgument);
} else {
  console.log('No argument');
}
