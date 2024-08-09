let input = require("fs").readFileSync("stdin", "utf8");
let lines = input.split("\n");

let amigos = 0;
let soma = 0;

for (let i = 0; i < lines.length; i+=2){
    let num = parseInt(lines[i+1]);
    if (isNaN(num)){
        continue;
    }
    else{
        soma+=num;
        amigos++;
    }
}

let result = (soma/amigos).toFixed(1);

console.log(result);