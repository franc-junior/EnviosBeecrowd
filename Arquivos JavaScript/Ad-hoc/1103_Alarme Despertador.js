let input = require("fs").readFileSync("stdin","utf8");
let lines = input.split("\n");

for (let i of lines){
    if (i == "0 0 0 0"){
        break;
    }

    let numeros = (i.split(" ")).map((num) => parseInt(num));
    const inicio = { hora: numeros.shift(), minuto: numeros.shift()}
    const fim = { hora: numeros.shift(), minuto: numeros.shift()}

    let diferenca = ((fim.hora*60)+fim.minuto)-((inicio.hora*60)+inicio.minuto)

    if (diferenca < 0){
        diferenca += 24*60
    }
    else if(isNaN(diferenca) || (diferenca === -0)){
        continue;
    }

    console.log(diferenca);
}