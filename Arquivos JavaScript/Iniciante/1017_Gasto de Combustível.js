var input = require("fs").readFileSync("stdin", "utf8");

var lines = input.split("\n");

var tempo = parseFloat(lines.shift());
var veloc = parseFloat(lines.shift());

var litros = (tempo*veloc)/12;

console.log(litros.toFixed(3));