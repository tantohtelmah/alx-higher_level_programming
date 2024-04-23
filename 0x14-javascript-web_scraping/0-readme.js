#!/usr/bin/node

const fs = require('fs');

function readAndPrintFileContent (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(`Error reading the file: ${err.message}`);
    } else {
      console.log(data);
    }
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];
readAndPrintFileContent(filePath);
