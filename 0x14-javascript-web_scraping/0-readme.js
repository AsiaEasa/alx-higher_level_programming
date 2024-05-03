#!/usr/bin/node

const files = require('fs');

files.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  process.stdout.write(data);
});
