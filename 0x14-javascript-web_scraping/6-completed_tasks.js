#!/usr/bin/node

const request = require('request');

function computeCompletedTasksByUser (url) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.error(`${error.message}`);
    } else if (response.statusCode === 200) {
      const todos = JSON.parse(body);
      const completedTasksByUser = {};

      for (const todo of todos) {
        if (todo.completed) {
          const userId = todo.userId;
          completedTasksByUser[userId] = completedTasksByUser[userId] || 0;
          completedTasksByUser[userId]++;
        }
      }
      console.log(completedTasksByUser);
    } else {
      console.error(`${response.statusCode}`);
    }
  });
}
const url = process.argv[2];
computeCompletedTasksByUser(url);
