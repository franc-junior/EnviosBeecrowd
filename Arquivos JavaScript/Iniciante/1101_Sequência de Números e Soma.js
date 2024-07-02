let input = require("fs").readFileSync("stdin", "utf8");
let lines = input.split("\n");

while (true){
    let caso = lines.shift().split(" ");
    let m = parseInt(caso[0]);
    let n = parseInt(caso[1]);

    if ((n <= 0) || (m <= 0)){
        break;
    }

    maior = Math.max(m,n);
    menor = Math.min(m,n);
    
    let str = "";
    let cont = 0;
    for (;menor<=maior; menor+=1){
        str += menor+" ";
        cont += menor
    }
    console.log(str+"Sum="+cont);
}