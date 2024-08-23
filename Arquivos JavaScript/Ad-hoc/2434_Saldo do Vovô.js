let input = require("fs").readFileSync("stdin", "utf8");
let lines = input.split("\n");

let ini = (lines.shift().split(" ")).map((e) => parseInt(e));
let idas = ini.shift();
let sald = ini.shift();
let menor = sald;

let historico = lines.map((e) => parseInt(e));

for (let i = 0; i < idas; i++){
    sald += historico[i];
    if (sald < menor){
        menor = sald;
    }
}
console.log(menor);


