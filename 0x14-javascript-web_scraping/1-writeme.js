#!/usr/bin/node

const files = require('fs');

files.writeFile(process.argv[2], process.argv[3], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
});
