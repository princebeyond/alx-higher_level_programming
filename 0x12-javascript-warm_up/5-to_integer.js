#!/usr/bin/node
const { argv } = require('node:process');
const num = Math.floor(Number(argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
