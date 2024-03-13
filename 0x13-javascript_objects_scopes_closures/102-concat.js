#!/usr/bin/node

const fs = require('fs');

function concatFiles (file1Path, file2Path, destPath) {
  try {
    // Read content from the first source file
    const content1 = fs.readFileSync(file1Path, 'utf8');

    // Read content from the second source file
    const content2 = fs.readFileSync(file2Path, 'utf8');

    // Concatenate the contents
    const combinedContent = content1 + content2;

    // Write the combined content to the destination file
    fs.writeFileSync(destPath, combinedContent);

    console.log(`Files ${file1Path} and ${file2Path} successfully concatenated to ${destPath}`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

// Usage: node concat_files.js <file1_path> <file2_path> <dest_path>
const [,, file1Path, file2Path, destPath] = process.argv;
concatFiles(file1Path, file2Path, destPath);
