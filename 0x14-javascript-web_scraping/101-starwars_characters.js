#!/usr/bin/node

const request = require('request');

// Function to get characters for a movie
function getMovieCharacters (movieId) {
  // API URL for Star Wars movies
  const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId + '/';

  // Send a GET request to the API URL
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error fetching data: ' + error);
      return;
    }

    // Parse the response body
    const data = JSON.parse(body);

    // Get the list of characters
    const characters = data.characters;

    // Print each character name
    characters.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
          return;
        }
        const charData = JSON.parse(charBody);
        console.log(charData.name);
      });
    });
  });
}

const movieID = process.argv[2];
getMovieCharacters(movieID);
