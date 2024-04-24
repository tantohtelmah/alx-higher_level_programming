#!/usr/bin/node

const request = require('request');
const fs = require('fs');

function saveWebpageToFile (url, filePath) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.error(`${error.message}`);
    } else if (response.statusCode === 200) {
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          console.error(`${err.message}`);
        }
      });
    } else {
      console.error(`${response.statusCode}`);
    }
  });
}

if (process.argv.length !== 4) {
  console.error('Usage: node script.js <url> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];
saveWebpageToFile(url, filePath);
