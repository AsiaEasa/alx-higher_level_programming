#!/usr/bin/node
// Status Of Get request

const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    process.stdout.write('code: ' + response.statusCode);
  }
  console.log(); // Print an empty line
});
