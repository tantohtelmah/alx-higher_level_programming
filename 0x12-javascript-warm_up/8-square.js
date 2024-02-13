#!/usr/bin/node

function printSquare(size) {
	const parsedSize = parseInt(size);
  
	if (isNaN(parsedSize)) {
	  console.log("Missing size");
	  return;
	}
  
	for (let i = 0; i < parsedSize; i++) {
	  let row = "";
	  for (let j = 0; j < parsedSize; j++) {
		row += "X";
	  }
	  console.log(row);
	}
  }
  
  // Example usage:
  printSquare(process.argv[2]);
  