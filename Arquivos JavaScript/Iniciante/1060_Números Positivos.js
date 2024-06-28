var input = require("fs").readFileSync("stdin", "utf8");
var lines = input.split("\n");
var cont = 0;

for (let i = 0; i < lines.length; i++){
    var valor = parseInt(lines[i]);
    if (valor >= 0){
        cont ++;
    }
}

console.log(cont+" valores positivos")