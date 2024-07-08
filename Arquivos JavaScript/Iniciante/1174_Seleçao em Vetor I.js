let input = require("fs").readFileSync("stdin", "utf8");
let lines = input.split("\n");

let cont = 0;
for (let i of lines){
    if (parseFloat(i) <= 10.0){
        console.log(`A[${cont}] = ${parseFloat(i).toFixed(1)}`);
    }
    cont++;
}