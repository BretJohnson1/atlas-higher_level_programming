#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const apiUrl = process.argv[2];
const file = process.argv[3];

request(apiUrl, function (err, response, body) {
  if (err) throw err;
  fs.writeFile(file, body, function (err) {
    if (err) throw err;
  });
});
