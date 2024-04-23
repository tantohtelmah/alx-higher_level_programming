#!/usr/bin/node

const fs = require('fs');

function writeStringToFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(`Error writing to the file: ${err.message}`);
    } else {
      console.log(`Content successfully written to ${filePath}`);
    }
  });
}

if (process.argv.length !== 4) {
  console.error('Usage: node script.js <file_path> <content>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];
writeStringToFile(filePath, content);
