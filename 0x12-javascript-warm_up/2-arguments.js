#!/usr/bin/node
cost process = require('process');
let args = process.argv;

if (args.length <= 1)
{
	console.log('No argument');
}
else if (args.length === 2)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}
