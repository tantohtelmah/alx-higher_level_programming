#!/usr/bin/node

const fs = require('fs');

function writeStringToFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(`${err.message}`);
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
