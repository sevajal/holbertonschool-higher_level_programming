#!/usr/bin/node
const axios = require('axios').default;

const id = process.argv[2];
axios.get(`https://swapi-api.hbtn.io/api/films/${id}`)
  .then((response) => {
    const characters = response.data.characters;
    async function getCharacters () {
      for (const character of characters) {
        const swcharacters = await axios.get(character);
        console.log(swcharacters.data.name);
      }
    }
    getCharacters();
  })
  .catch(function (error) {
    console.log(error);
  });
