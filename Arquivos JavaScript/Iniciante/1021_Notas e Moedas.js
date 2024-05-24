var input = require("fs").readFileSync("stdin","utf8");

var valor = parseFloat(input);

function resto(valor, n){
    var x = (valor*n)%n;
    return x;
}

var nDe100 = valor/100;
var nDe50 = resto(nDe100, 100)/50;
var nDe20 = resto(nDe50, 50)/20;
var nDe10 = resto(nDe20, 20)/10;
var nDe5 = resto(nDe10, 10)/5;
var nDe2 = resto(nDe5, 5)/2;

var mDe1 = resto(nDe2, 2)/1;
var mDe50 = (resto(mDe1, 1)/0.5)+0.001;
var mDe25 = (resto(mDe50, 0.5)/0.25)+0.001;
var mDe10 = (resto(mDe25, 0.25)/0.10)+0.001;
var mDe5 = (resto(mDe10, 0.10)/0.05)+0.001;
var mDe01 = resto(mDe5, 0.05)/0.01;

console.log("NOTAS:")

console.log(parseInt(nDe100) + " nota(s) de R$ 100.00");
console.log(parseInt(nDe50) + " nota(s) de R$ 50.00");
console.log(parseInt(nDe20) + " nota(s) de R$ 20.00");
console.log(parseInt(nDe10) + " nota(s) de R$ 10.00");
console.log(parseInt(nDe5) + " nota(s) de R$ 5.00");
console.log(parseInt(nDe2) + " nota(s) de R$ 2.00");

console.log("MOEDAS:")

console.log(parseInt(mDe1) + " moeda(s) de R$ 1.00");
console.log(parseInt(mDe50) + " moeda(s) de R$ 0.50");
console.log(parseInt(mDe25) + " moeda(s) de R$ 0.25");
console.log(parseInt(mDe10) + " moeda(s) de R$ 0.10");
console.log(parseInt(mDe5) + " moeda(s) de R$ 0.05");
console.log(parseInt(mDe01) + " moeda(s) de R$ 0.01");