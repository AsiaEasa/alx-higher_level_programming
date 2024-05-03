#!/usr/bin/node

const request = require('request');
const x = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + x;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const xx = JSON.parse(body);
    console.log(xx.title);
  }
});
