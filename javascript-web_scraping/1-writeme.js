#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const textWritten = process.argv[3];

fs.writeFile(filePath, textWritten, function (err) {
  if (err) throw err;
});
