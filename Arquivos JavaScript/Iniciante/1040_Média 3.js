var input = require("fs").readFileSync("stdin", "utf8");
var t = input.split("\n");

var valores = t.shift().split(" ");

var n1 = parseFloat(valores.shift());
var n2 = parseFloat(valores.shift());
var n3 = parseFloat(valores.shift());
var n4 = parseFloat(valores.shift());

var media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10;
console.log("Media: "+media.toFixed(1));

if (media >= 7.0){
    console.log("Aluno aprovado.");
}
else if (media < 5.0){
    console.log("Aluno reprovado.");
}
else{
    console.log("Aluno em exame.");
    var exame = parseFloat(t.shift());
    console.log("Nota do exame: "+exame.toFixed(1));
    var newMedia = (media+exame)/2;
    if (newMedia>=5.0){
        console.log("Aluno aprovado.");
    }
    else{
        console.log("Aluno reprovado.");
    }
    console.log("Media final: "+newMedia.toFixed(1));
}

