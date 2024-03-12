#!/usr/bin/node

// Define a recursive function to compute factorial
function factorial (n) {
  if (n === 0) {
    return 1; // Base case: factorial of 0 is 1
  } else {
    return n * factorial(n - 1); // Recursive case
  }
}

// Get the first argument from the command-line
const input = process.argv[2];
const num = parseInt(input, 10);

// Check if the conversion was successful
if (!isNaN(num)) {
  const result = factorial(num);
  console.log(`${result}`);
} else {
  console.log(1);
}
