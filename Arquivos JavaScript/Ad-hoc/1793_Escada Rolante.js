let input = require("fs").readFileSync("stdin", "utf8");
let lines = input.split("\n");

for (let i = 1; i < lines.length; i+=2){
    let lista = (lines[i].split(" ")).map((e) => parseInt(e));
    let soma = 10;
    let tam = lista.length-1;
    let ant = lista[tam];
   
    if (lines[i-1] == 0){
        break;
    }
    
    for (let i = tam-1; i >= 0 ; i--){
        let calc = ant-lista[i];

        if (calc >= 10){
            soma+=10;
        }
        else{
            soma+=calc;
        }
        ant = lista[i];
    }
    console.log(soma);       
}