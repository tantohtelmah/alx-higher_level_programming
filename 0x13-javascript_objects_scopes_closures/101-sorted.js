#!/usr/bin/node

// Assuming occurrences data is provided in 101-data.js
const occurrencesData = require('./101-data');

// Initialize a dictionary to store user IDs by occurrence
const userIDsByOccurrence = {};

// Iterate over the occurrences data
for (const userID in occurrencesData) {
  const occurrences = occurrencesData[userID];
  if (!userIDsByOccurrence[occurrences]) {
    userIDsByOccurrence[occurrences] = [userID];
  } else {
    userIDsByOccurrence[occurrences].push(userID);
  }
}

// Print the new dictionary
for (const occurrences in userIDsByOccurrence) {
  console.log(`Occurrences ${occurrences}: ${userIDsByOccurrence[occurrences]}`);
}
