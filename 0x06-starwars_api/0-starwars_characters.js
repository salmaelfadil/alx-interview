#!/usr/bin/node
const request = require('request');

let url = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];

function getData(url) {
    request(url, (error, response, body) => {
        if (error) {
            console.error(error);
            return;
        }
        try {
            const data = JSON.parse(body).characters;
            getChars(data);
        } catch (parseError) {
            console.error("Error Parsing");
        }
    });
}

function getChars(data) {
    data.forEach(url => {
        request(url, (error, response, body) => {
            if (error) {
                console.error(error);
                return;
            }
            try {
                const chars = JSON.parse(body);
                console.log(chars.name);
            } catch (parseError) {
                console.error("Error parsing JSON");
            }
        });
    });
}

getData(url);

