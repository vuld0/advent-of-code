const path = require('path');
const fs = require('fs');

// const input = fs.readFileSync(path.join(__dirname, 'input1.txt'), 'utf-8').toString().trim().split('\n').map((num) => parseInt(num, 10));

const input = fs.readFileSync(path.join(__dirname, 'input1.txt'), 'utf-8').toString().trim().split('\n').map((num) => parseInt(num, 10));

console.log(input)

module.exports = {
    input,
}