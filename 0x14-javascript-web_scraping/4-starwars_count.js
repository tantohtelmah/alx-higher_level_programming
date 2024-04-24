#!/usr/bin/node
const request = require('request');

function getMovieCountForCharacter (apiUrl) {
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(`${error.message}`);
    } else if (response.statusCode === 200) {
      const movies = JSON.parse(body).results;
      const filteredMovies = movies.filter(movie =>
        movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );
      console.log(`${filteredMovies.length}`);
    } else {
      console.error(`Error fetching data. Status code: ${response.statusCode}`);
    }
  });
}

const url = process.argv[2];
getMovieCountForCharacter(url);
