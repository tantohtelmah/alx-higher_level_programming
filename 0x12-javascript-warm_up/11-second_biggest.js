#!/usr/bin/node

// Get the command-line arguments (excluding the script name)
const args = process.argv.slice(2);

// Convert arguments to integers and filter out non-numeric values
const numbers = args.map(Number).filter(num => !isNaN(num));

// Sort the numbers in descending order
numbers.sort((a, b) => b - a);

// Print the second largest integer or 0 if not found
console.log(numbers[1] || 0);
