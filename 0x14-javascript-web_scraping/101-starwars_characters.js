#!/usr/bin/node
const axios = require('axios').default;

const id = process.argv[2];
axios.get(`https://swapi-api.hbtn.io/api/films/${id}`)
  .then(function (response) {
    for (let i = 0; response.data.characters[i]; i++) {
      axios.get(response.data.characters[i])
        .then(function (swcharacters) {
          console.log(swcharacters.data.name);
        });
    }
  })
  .catch(function (error) {
    console.log(error);
  });
