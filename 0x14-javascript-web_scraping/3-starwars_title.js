#!/usr/bin/node

const request = require('request');

function getMovieTitle (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(`${error.message}`);
    } else if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(`${movieData.title}`);
    } else {
      console.error(`${response.statusCode}`);
    }
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
getMovieTitle(movieId);
