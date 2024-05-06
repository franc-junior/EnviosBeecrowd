var input = require("fs").readFileSync("stdin", "utf8");
var valores = input.split("\n");

var a = parseFloat(valores[0])*3.5;
var b = parseFloat(valores[1])*7.5;

console.log("MEDIA = "+(((a+b)/11).toFixed(5)));