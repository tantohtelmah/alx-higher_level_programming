#!/usr/bin/node

function printConvertedNumber() {
	const firstArg = process.argv[2];
	const parsedNumber = parseInt(firstArg);
  
	if (!isNaN(parsedNumber)) {
	  console.log(`My number: ${parsedNumber}`);
	} else {
	  console.log("Not a number");
	}
  }
  