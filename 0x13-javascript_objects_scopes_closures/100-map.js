#!/usr/bin/node

const list = require('./100-map').list;
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log('Initial list:', list);
console.log('New list:', newList);
