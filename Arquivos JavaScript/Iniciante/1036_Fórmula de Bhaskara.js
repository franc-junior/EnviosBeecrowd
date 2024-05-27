var input = require("fs").readFileSync("stdin", "utf8");

var valores = input.split(" ");
var a = parseFloat(valores.shift()), b = parseFloat(valores.shift()), c = parseFloat(valores.shift());

if (a === 0 || (b ** 2 - 4 * a * c) < 0){
    console.log("Impossivel calcular");
}

else{
    var delta = b ** 2 - 4 * a * c;
    var x1 = (- b + (delta ** 0.5)) / (2 * a);
    var x2 = (- b - (delta ** 0.5)) / (2 * a);

    console.log(`R1 = ${x1.toFixed(5)}\nR2 = ${x2.toFixed(5)}`)
}