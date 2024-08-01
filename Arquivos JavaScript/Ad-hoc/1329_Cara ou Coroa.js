let input = require("fs").readFileSync("stdin", "utf8");
let lines = input.split("\n");

while (true){
    let n = parseInt(lines.shift());
    if (n === 0){
        break;
    }
    let casos = (lines.shift()).split(" ");
    const qtd = casos.filter(i => i == "0").length;
    console.log(`Mary won ${qtd} times and John won ${n-qtd} times`);
    
}