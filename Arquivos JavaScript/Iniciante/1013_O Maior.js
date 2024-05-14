var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split(" ");
var a = parseInt(valores.shift());
var b = parseInt(valores.shift());
var c = parseInt(valores.shift());

var maiorAB = (a+b+Math.abs(a-b))/2;
var maiorGeral = (maiorAB+c+Math.abs(maiorAB-c))/2;

console.log(maiorGeral + " eh o maior");


