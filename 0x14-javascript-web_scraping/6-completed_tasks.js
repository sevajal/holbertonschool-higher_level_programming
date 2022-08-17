#!/usr/bin/node
const axios = require('axios').default;
const result = {};
axios.get(process.argv[2])
  .then(function (response) {
    for (let i = 0; response.data[i]; i++) {
      if (response.data[i].completed === true) {
        if (!result[response.data[i].userId]) {
          result[response.data[i].userId] = 1;
        } else {
          result[response.data[i].userId] += 1;
        }
      }
    }
    console.log(result);
  })
  .catch(function (error) {
    console.log(error);
  });
