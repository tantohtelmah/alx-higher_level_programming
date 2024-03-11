#!/usr/bin/node

// Get the first argument from the command-line
const firstArgument = process.argv[2];

// Convert the argument to an integer
const size = parseInt(firstArgument, 10);

// Check if the conversion was successful
if (!isNaN(size)) {
  // Print the square using 'X'
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let j = 0; j < size; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
