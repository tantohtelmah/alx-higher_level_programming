#!/usr/bin/node

// Import the list from 100-data.js
const { list } = require('./100-data');

// Compute a new list using a map (value * index)
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log('Initial list:', list);
console.log('New list:', newList);
