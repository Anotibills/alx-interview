#!/usr/bin/node

const request = require('request');

// This ensure a film number is provided as a command-line argument
if (process.argv.length < 3) {
  console.error("Please provide a film number as a command-line argument.");
  process.exit(1);
}

const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi.dev/api/films/';

// This makes API request, sets async to allow await promise
request(filmURL + filmNum, async (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  try {
    const filmData = JSON.parse(body);
    
    // This check if film data is fetched successfully
    if (!filmData || !filmData.characters || filmData.characters.length === 0) {
      console.error("No character data found for the provided film number.");
      return;
    }

    const charURLList = filmData.characters;

    // This use URL list to character pages to make new requests
    // And also await queues requests until they resolve in order
    for (const charURL of charURLList) {
      await new Promise((resolve, reject) => {
        request(charURL, (err, res, body) => {
          if (err) {
            console.error(err);
            reject(err);
            return;
          }

          // This parse character data and print name
          const character = JSON.parse(body);
          if (character && character.name) {
            console.log(character.name);
          }
          resolve();
        });
      });
    }
  } catch (error) {
    console.error("Error occurred while processing film data:", error);
  }
});
