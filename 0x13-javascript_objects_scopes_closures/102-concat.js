#!/usr/bin/node

const fs = require('fs');

function concatenateFiles(sourceFile1, sourceFile2, destinationFile) {
  try {
    // Read the contents of the first source file
    const content1 = fs.readFileSync(sourceFile1, 'utf8');

    // Read the contents of the second source file
    const content2 = fs.readFileSync(sourceFile2, 'utf8');

    // Concatenate the contents
    const concatenatedContent = content1 + content2;

    // Write the concatenated content to the destination file
    fs.writeFileSync(destinationFile, concatenatedContent, 'utf8');

    console.log(`Files successfully concatenated. Result saved in ${destinationFile}`);
  } catch (error) {
    console.error('Error concatenating files:', error.message);
  }
}
