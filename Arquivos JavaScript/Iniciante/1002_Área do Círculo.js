var input = require("fs").readFileSync("stdin", "utf8");
var raio = input;
var pi = 3.14159;
var area = pi*(raio**2);

console.log("A="+area.toFixed(4)); // limita a quantidade de casas decimais após o ponto
