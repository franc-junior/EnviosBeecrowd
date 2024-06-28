var input = require("fs").readFileSync("stdin", "utf8");

for (var i = 1; i<=parseInt(input); i+=2){
    console.log(i);
}