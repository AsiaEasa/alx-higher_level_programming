#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (!error) {
    const F = JSON.parse(body).results;
    const characterFilms = F.filter(film => {
      for (const char of film.characters) {
        if (char.endsWith('/18/')) {
          return true;
        }
      }
      return false;
    });
    console.log(characterFilms.length);
  }
});
