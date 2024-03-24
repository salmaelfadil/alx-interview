#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function getData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      try {
        const characters = JSON.parse(body).characters;
        resolve(characters);
      } catch (parseError) {
        reject(new Error('Error parsing film data'));
      }
    });
  });
}

function getChars (characters) {
  const promises = characters.map(url => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        try {
          const character = JSON.parse(body);
          resolve(character.name);
        } catch (parseError) {
          reject(new Error('Error parsing character data'));
        }
      });
    });
  });
  Promise.all(promises)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => console.error(error));
}
getData(url)
  .then(getChars)
  .catch(error => console.error(error));
