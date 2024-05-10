var input = require("fs").readFileSync("stdin", "utf8");
var valores = input.split("\n");

var num = parseInt(valores.shift());
var horas = parseInt(valores.shift());
var qt = parseFloat(valores.shift());

console.log("NUMBER = " + num + "\nSALARY = U$ " + (horas*qt).toFixed(2));