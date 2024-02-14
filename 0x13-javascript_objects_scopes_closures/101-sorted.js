#!/usr/bin/node

// compute_occurrences.js

// Import the input dictionary from 101-data.js
const inputDictionary = require('./101-data.js');

// Initialize an empty dictionary to store occurrences
const occurrencesDictionary = {};

// Iterate through the user IDs in the input dictionary
for (const userId in inputDictionary) {
  const occurrences = inputDictionary[userId];

  // If the occurrences count is not already a key in the occurrencesDictionary, create it
  if (!occurrencesDictionary[occurrences]) {
    occurrencesDictionary[occurrences] = [];
  }

  // Add the current user ID to the list of user IDs with the same occurrences count
  occurrencesDictionary[occurrences].push(userId);
}

// Print the occurrencesDictionary
console.log(occurrencesDictionary);
