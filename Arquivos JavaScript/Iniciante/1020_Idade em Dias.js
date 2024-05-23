var input = require("fs").readFileSync("stdin", "utf8");

var totalDias = parseInt(input);

var anos = parseInt(totalDias/365);
var meses = parseInt((totalDias%365)/30);
var dias = parseInt((totalDias%365)%30);

console.log(anos+" ano(s)");
console.log(meses+" mes(es)");
console.log(dias+" dia(s)");