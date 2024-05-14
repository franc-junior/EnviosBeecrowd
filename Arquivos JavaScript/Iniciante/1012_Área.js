var input = require("fs").readFileSync("stdin", "utf8");

var valores, a, b, c, pi = 3.14159, triRetan, circulo, trapezio, quadrado, retangulo; 

valores = input.split(" ");
a = parseFloat(valores.shift());
b = parseFloat(valores.shift());
c = parseFloat(valores.shift());

triRetan = (a * c) / 2;
circulo = pi * c ** 2;
trapezio = ((a + b) * c) / 2;
quadrado = b * b;
retangulo = a * b;

console.log(
    "TRIANGULO: " + triRetan.toFixed(3) +
    "\nCIRCULO: " + circulo.toFixed(3) +
    "\nTRAPEZIO: " + trapezio.toFixed(3) +
    "\nQUADRADO: " + quadrado.toFixed(3) +
    "\nRETANGULO: " + retangulo.toFixed(3)
);
