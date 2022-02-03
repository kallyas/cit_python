const fs = require('fs');

// read data.json
const data = fs.readFileSync('data.json');

// parse data.json
const dataJson = JSON.parse(data);

// map and return an array of objects containing only the name and capital
const dataJsonMap = dataJson.map(function(item) {
  return {
    name: item.name,
    capital: item.capital
  };
});

// overwrite data.json
fs.writeFileSync('data.json', JSON.stringify(dataJsonMap));