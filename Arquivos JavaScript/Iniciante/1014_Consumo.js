var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split("\n");

var a = parseInt(valores.shift());
var b = parseFloat(valores.shift());

var consumo = (a/b).toFixed(3);

console.log(consumo + " km/l");