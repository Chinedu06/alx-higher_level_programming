#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;
    characters.forEach(url => {
      request.get(url, (err, res, b) => {
        if (err) {
          console.error(err);
        } else {
          const character = JSON.parse(b);
          console.log(character.name);
        }
      });
    });
  }
});
