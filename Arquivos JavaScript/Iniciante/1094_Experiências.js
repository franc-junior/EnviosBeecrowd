var input = require("fs").readFileSync("stdin", "utf8");
let lines = input.split("\n");

let repet = parseInt(lines.shift());
let coelho = 0, rato = 0, sapo = 0;

for (let i = 0; i < repet; i++){
    let caso = lines[i].split(" ");
    let num = parseInt(caso.shift());
    let bixo = caso.shift().trim();

    switch (bixo){
        case "C":
            coelho += num;
            break;
        case "S":
            sapo += num;
            break;
        case "R":
            rato += num;
    }
    
}
let total = coelho+sapo+rato;

console.log(`Total: ${total} cobaias
Total de coelhos: ${coelho}
Total de ratos: ${rato}
Total de sapos: ${sapo}
Percentual de coelhos: ${((coelho/total)*100).toFixed(2)} %
Percentual de ratos: ${((rato/total)*100).toFixed(2)} %
Percentual de sapos: ${((sapo/total)*100).toFixed(2)} %`)