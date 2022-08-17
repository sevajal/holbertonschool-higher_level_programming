#!/usr/bin/node
const axios = require('axios').default;
let count = 0;
axios.get(process.argv[2])
  .then(function (response) {
    for (let i = 0; i < response.data.results.length; i++) {
      const obj = response.data.results[i].characters;
      obj.forEach((link) => {
        if (link.search('18') !== -1) {
          count++;
        }
      });
    }
    console.log(count);
  })
  .catch(function (error) {
    console.log(error);
  });
