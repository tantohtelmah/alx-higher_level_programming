#!/usr/bin/node

const executeXTimes = (x, theFunction) => {
	for (let i = 0; i < x; i++) {
	  theFunction();
	}
  };
  
  // Example usage:
  const printHello = () => {
	console.log("Hello!");
  };
  
  executeXTimes(5, printHello); // Calls printHello 5 times
  