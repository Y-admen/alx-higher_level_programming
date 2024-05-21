#!/usr/bin/node

const fs = require('fs'); // Import the File System module

const path = process.argv[2]; // Get the file path from command line arguments

fs.readFile(path, 'utf-8', (err, data) => {
	if (err) {
		console.error(err);  // Print the error object
	} else {
		console.log(data); // Print the file content
	}
});
