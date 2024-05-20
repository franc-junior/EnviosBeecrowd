var input = require("fs").readFileSync("stdin", "utf8");

var segundos = parseInt(input);

var horas = parseInt(segundos/(60*60));
var minutos = parseInt((segundos%(60*60))/60);
segundos %= 60;


console.log(`${horas}:${minutos}:${segundos}`);

