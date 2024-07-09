let input = require("fs").readFileSync("stdin","utf8");
let lines = input.split("\n").map((valor) => parseInt(valor));

let n = lines.shift();
let numeros = [...new Set(lines)].sort((a, b) => a-b);
let cont = 0;

for (let i of numeros){    
    if (isNaN(i)){
        continue;
    }
    for (let j of lines){
        if (i===j){
            cont++;
        }
    }
    console.log(`${i} aparece ${cont} vez(es)`);
    cont = 0;
}



