let input = require("fs").readFileSync("stdin", "utf8");
let lines = input.split("\n");

let n = parseInt(lines.shift());
let numberis = (lines.shift()).split(" ");

const menor = {
    valor: parseInt(numberis[0]),
    posicao: 0
}

for(let i = 1; i < n; i++){
    let valor = parseInt(numberis[i])
    if(valor < menor.valor){
        menor.valor = valor;
        menor.posicao = i;
    }
}
console.log("Menor valor: "+menor.valor+"\nPosicao: "+menor.posicao);