var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split(" ");

var a = parseInt(valores.shift()), b = parseInt(valores.shift()), c = parseInt(valores.shift()), d = parseInt(valores.shift());

if (b > c && d > a && (c+d) > (a+b) && c>0 && d>0 && a%2===0) {
    console.log("Valores aceitos");
} else {
    console.log("Valores nao aceitos")
}