#!/usr/bin/node
const axios = require('axios');

// Base URL for the Star Wars API
const BASE_URL = 'https://swapi-api.alx-tools.com/api';

/**
 * Fetches the details of a specific film by its ID.
 * @param {number|string} filmId - The ID of the film.
 * @returns {Promise<Object|null>} A promise that resolves to the film details object or null if an error occurs.
 */
async function getFilmDetails (filmId) {
  try {
    const response = await axios.get(`${BASE_URL}/films/${filmId}/`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching film details: ${error.response.status}`);
    return null;
  }
}

/**
 * Fetches the name of a character given its URL.
 * @param {string} url - The URL of the character resource.
 * @returns {Promise<string|null>} A promise that resolves to the character's name or null if an error occurs.
 */
async function getCharacterName (url) {
  try {
    const response = await axios.get(url);
    return response.data.name;
  } catch (error) {
    console.error(`Error fetching character details: ${error.response.status}`);
    return null;
  }
}

/**
 * Prints the names of all characters in a specified Star Wars film.
 * @param {number|string} filmId - The ID of the film.
 * @returns {Promise<void>}
 */
async function printCharacters (filmId) {
  const filmDetails = await getFilmDetails(filmId);
  if (filmDetails) {
    const characterUrls = filmDetails.characters;
    for (const url of characterUrls) {
      const name = await getCharacterName(url);
      if (name) {
        console.log(name);
      }
    }
  }
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <Movie ID>');
  process.exit(1);
}

const filmId = process.argv[2];
printCharacters(filmId);
