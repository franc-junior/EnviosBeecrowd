var input = require("fs").readFileSync("stdin", "utf8");
var lines = input.split("\n");
var cont = 0;
var somaPositivos = 0;

for (let i = 0; i < lines.length; i++){
    var valor = parseFloat(lines[i]);
    if (valor >= 0){
        cont ++;
        somaPositivos += valor;
    }
}

console.log(cont+" valores positivos\n"+ (somaPositivos/cont).toFixed(1));