let input = require("fs").readFileSync("stdin", "utf8");
let lines = input.split("\n");

let nc = parseInt(lines.shift());

function mata(lista, pulos){
    lista = [...lista, ...lista.splice(0, pulos-1)];
    lista.splice(0, pulos-1);
    lista.shift();
    if (lista.length > 1){
        /* console.log(lista) */
        return mata(lista, pulos);
    }
    else{
        return lista;
    }
}

function pessoas(caso){
    let lista = [];
    for (let i = 0; i<caso.n_peso; i++){
        lista.push(i);
    }
    return mata(lista, caso.pulos);
}

for (let i = 0; i < nc; i++){
    let c = lines[i].split(" ");
    const caso = {
        n_peso: parseInt(c[0]),
        pulos: parseInt(c[1])
    }
    console.log(pessoas(caso)[0]+1);
}