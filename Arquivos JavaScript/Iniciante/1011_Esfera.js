var input = require("fs").readFileSync("stdin", "utf8");

var pi = 3.14159;

volume = (4.0/3.0)*pi*(input**3);

console.log("VOLUME = " + volume.toFixed(3));