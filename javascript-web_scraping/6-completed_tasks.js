#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (err, response, body) {
  if (err) throw err;
  const users = {};
  // Converts the response body to JSON and iterates over tasks
  for (const task of JSON.parse(body)) {
    // Checks if the task is completed and associated with a user
    if (task.completed && task.userId) {
      // If the user already exists in the users object, increment the count
      if (users[task.userId]) {
        users[task.userId]++;
      } else {
        users[task.userId] = 1;
      }
    }
  }
  console.log(users);
});
