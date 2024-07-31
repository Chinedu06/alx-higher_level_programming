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
    const characterNames = [];

    characters.forEach((url, index) => {
      request.get(url, (err, res, b) => {
        if (err) {
          console.error(err);
        } else {
          const character = JSON.parse(b);
          characterNames[index] = character.name;

          if (characterNames.filter(name => name).length === characters.length) {
            characterNames.forEach(name => console.log(name));
          }
        }
      });
    });
  }
});
