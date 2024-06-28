function conversor(inicio, final){
    var hora = parseInt(((final.hora+final.minutos)-(inicio.hora+inicio.minutos)));

    if (hora < 0){
        hora = hora+(24*60);
    }
    if (hora === 0){
        hora = 24*60;
    }
    console.log(`O JOGO DUROU ${parseInt(parseInt(hora/60))} HORA(S) E ${hora%60} MINUTO(S)`);
}

var input = require("fs").readFileSync("stdin", "utf8");
var valores = input.split(" ");

const inicio = {
    hora: parseInt(valores.shift())*60,
    minutos: parseInt(valores.shift())
};
const final = {
    hora: parseInt(valores.shift())*60,
    minutos: parseInt(valores.shift())
};

conversor(inicio, final);
