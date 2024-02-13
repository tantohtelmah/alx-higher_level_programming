#!/usr/bin/node

function factorial(n) {
	if (n < 0) {
	  return; // Factorial of negative numbers does not exist
	}
  
	if (n === 0) {
	  return 1; // Factorial of 0 is 1
	}
  
	return n * factorial(n - 1);
  }
  
  // Example usage:
  const num = parseInt(process.argv[2]);
  if (!isNaN(num)) {
	const result = factorial(num);
	console.log(`The factorial of ${num} is: ${result}`);
  } else {
	console.log("Missing number of occurrences");
  }
  