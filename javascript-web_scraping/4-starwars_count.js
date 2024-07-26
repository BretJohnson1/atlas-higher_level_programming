#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, data) {
  if (err) {
    console.error(err);
  } else {
    const json = JSON.parse(data).results;
    let countWedge = 0;
    for (const movie in json) {
      const characters = json[movie].characters;
      for (const person in characters) {
        if (characters[person].includes('/18/')) {
          countWedge += 1;
        }
      }
    }
    console.log(countWedge);
  }
});