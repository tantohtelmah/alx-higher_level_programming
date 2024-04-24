#!/usr/bin/node

const request = require('request');

function displayStatusCode (url) {
  request.get(url, (error, response) => {
    if (error) {
      console.error(`${error.message}`);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <url>');
  process.exit(1);
}

const url = process.argv[2];
displayStatusCode(url);
