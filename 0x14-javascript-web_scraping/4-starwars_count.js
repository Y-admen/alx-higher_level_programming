#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
let count = 0;
req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const obj = JSON.parse(body);
  const results = obj.results; // accessing the result
  results.forEach(film => { // looping through result
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  });
  console.log(count);
});
