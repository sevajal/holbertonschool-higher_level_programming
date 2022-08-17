#!/usr/bin/node
const axios = require('axios').default;
const fs = require('fs');

axios({
  method: 'get',
  url: process.argv[2],
  responseType: 'stream'
}).then(function (response) {
  response.data.pipe(fs.createWriteStream(process.argv[3]));
});
