#!/usr/bin/node
const axios = require('axios').default;
const result = {};
axios.get(process.argv[2])
  .then((response) => {
    const tasks = response.data;
    for (const task of tasks) {
      if (task.completed) {
        if (!result[task.userId]) {
          result[task.userId] = 1;
        } else {
          result[task.userId]++;
        }
      }
    }
    console.log(result);
  })
  .catch(function (error) {
    console.log(error);
  });
