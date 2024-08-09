var input = parseFloat(require('fs').readFileSync('stdin', 'utf8'));

let porc;
if (input >= 0 && input <= 400.00){
  porc = 15;
}else if (input <= 800.00){
  porc = 12;
}else if (input <= 1200.00){
  porc = 10;
}else if (input <= 2000.00){
  porc = 7;
}else{
  porc = 4;
}
let valor = input*(porc/100);

console.log(`Novo salario: ${(input+valor).toFixed(2)}`);
console.log(`Reajuste ganho: ${(valor).toFixed(2)}`);
console.log(`Em percentual: ${porc} %`);