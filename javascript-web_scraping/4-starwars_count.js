#!/usr/bin/node
const request = require('request');
const characterId = '18/';
const filmApiUrl = process.argv[2];
const characterApiUrl = 'https://swapi-api.hbtn.io/api/people/';

request(filmApiUrl, function (err, response, body) {
  if (!err && response.statusCode === 200) {
    // Convert the data to JSON
    const films = JSON.parse(body).results;
    // Initialize movieCount
    let movieCount = 0;
    // Iterating over each film to find matching character id
    films.forEach(function (film) {
      // Find the characters for each movie
      const characters = film.characters;
      // Check if the characterId exists in the characters array
      if (characters.includes(characterApiUrl + characterId)) {
        movieCount++;
      }
    });
    console.log(movieCount);
  }
});
