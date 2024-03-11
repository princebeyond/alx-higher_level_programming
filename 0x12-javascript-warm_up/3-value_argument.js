#!/usr/bin/node
const { argv } = require('node:process');
let i;
let flag = false;
for (i of argv)
{
	if (i == argv[2])
	{
		flag = true;
	}
}
if (flag == true)
{
	console.log(argv[2]);
} else
{
	console.log('No argument');
}
