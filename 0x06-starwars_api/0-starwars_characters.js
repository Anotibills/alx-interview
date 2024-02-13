#!/usr/bin/node

const request = require('request');

// Get the film number from command line arguments
const filmNum = process.argv[2];
const filmURL = `https://swapi.dev/api/films/${filmNum}/`;

// Function to fetch character information
async function fetchCharacterInfo(charURL) {
  return new Promise((resolve, reject) => {
    request(charURL, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}

// Make an API request to get film information
request(filmURL, async (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  // Parse the response body to get the list of character URLs
  const characters = JSON.parse(body).characters;

  try {
    // Iterate through the character URLs and fetch character information
    for (const charURL of characters) {
      const characterName = await fetchCharacterInfo(charURL);
      console.log(characterName);
    }
  } catch (error) {
    console.error(error);
  }
});
