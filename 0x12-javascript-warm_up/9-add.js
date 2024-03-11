#!/usr/bin/node

// Define a function to add two integers
function add (a, b) {
  return a + b;
}

// Get the first and second arguments from the command-line
const firstArgument = process.argv[2];
const secondArgument = process.argv[3];

// Convert the arguments to integers
const num1 = parseInt(firstArgument, 10);
const num2 = parseInt(secondArgument, 10);

// Check if the conversion was successful
if (!isNaN(num1) && !isNaN(num2)) {
  // Call the add function and print the result
  const result = add(num1, num2);
  console.log(`${result}`);
} else {
  console.log('NaN');
}
