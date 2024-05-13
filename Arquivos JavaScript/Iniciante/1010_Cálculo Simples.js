var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split("\n");
var linha1 = valores.shift().split(" ");
var linha2 = valores.shift().split(" ");

var qt1 = parseInt(linha1[1]);
var vr1 = parseFloat(linha1[2]);

var qt2 = parseInt(linha2[1]);
var vr2 = parseFloat(linha2[2]);

total = (qt1 * vr1) + (qt2 * vr2);

console.log("VALOR A PAGAR: R$ " + total.toFixed(2));
