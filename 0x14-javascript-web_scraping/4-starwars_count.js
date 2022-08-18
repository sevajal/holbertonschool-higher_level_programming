#!/usr/bin/node
const axios = require('axios').default;
let count = 0;
axios.get(process.argv[2])
  .then((response) => {
    const films = response.data.results;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  })
  .catch(function (error) {
    console.log(error);
  });
