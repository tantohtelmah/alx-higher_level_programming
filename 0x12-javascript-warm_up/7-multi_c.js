#!/usr/bin/node

// Get the first argument from the command-line
const firstArgument = process.argv[2];

// Convert the argument to an integer
const numOccurrences = parseInt(firstArgument, 10);

// Check if the conversion was successful
if (!isNaN(numOccurrences)) {
  // Print "C is fun" x times
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
