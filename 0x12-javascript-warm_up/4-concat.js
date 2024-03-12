#!/usr/bin/node

// Get the first and second arguments from the command-line
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Check if both arguments are provided
if (arg1 !== undefined && arg2 !== undefined) {
  console.log(`${arg1} is ${arg2}`);
} else {
  console.log("undefined is undefined");
}
