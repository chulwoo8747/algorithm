var fs = require('fs'); 
var input = fs.readFileSync('/dev/stdin').toString().split('\n'); 
input.pop()
var a = parseInt(input[0]); 
for (let i =1;i<=a; i++) {
    let sp = input[i].split(' ')
    console.log(parseInt(sp[0]) + parseInt(sp[1]))
}