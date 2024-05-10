var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split("\n");

nome = valores.shift();
fixo = parseFloat(valores.shift());
total = parseFloat(valores.shift());

bonus = ((total*15)/100)+fixo;

console.log("TOTAL = R$ " + bonus.toFixed(2));