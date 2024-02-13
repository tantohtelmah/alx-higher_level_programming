#!/usr/bin/node

function printFirstArgument() {
	if (arguments[0] === undefined) {
	  console.log("No argument");
	} else {
	  console.log(arguments[0]);
	}
  }