#!/usr/bin/node

function findSecondLargest() {
	const args = process.argv.slice(2); // Exclude the first two arguments (node and script name)
	const integers = args.map(Number).filter(Number.isInteger);
  
	if (integers.length === 0) {
	  console.log(0);
	} else if (integers.length === 1) {
	  console.log(0);
	} else {
	  integers.sort((a, b) => b - a); // Sort in descending order
	  console.log(integers[1]);
	}
  }
  
  findSecondLargest();
  