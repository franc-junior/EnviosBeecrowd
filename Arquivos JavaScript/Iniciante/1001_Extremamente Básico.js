var input = require("fs").readFileSync("stdin", "utf8");
/* 
    require("fs"): O require é uma função do Node.js que é usada para importar (ou requerer) módulos. Aqui, estamos importando o módulo fs, que fornece funcionalidades para interagir com o sistema de arquivos do sistema operacional.
    readFileSync("stdin", "utf8"): readFileSync é um método do módulo fs que lê um arquivo de forma síncrona (bloqueante), ou seja, o código aguarda até que a leitura do arquivo seja concluída antes de continuar. Neste caso, estamos lendo do arquivo "stdin". "stdin" é uma convenção usada em sistemas Unix e Linux para representar a entrada padrão, que normalmente é o terminal.
    "utf8" é um parâmetro opcional que especifica a codificação do arquivo. Neste caso, estamos usando a codificação UTF-8 para decodificar os bytes lidos e convertê-los em caracteres legíveis.
    var input = ...: Estamos atribuindo o resultado da leitura do arquivo à variável input. Isso significa que input conterá o conteúdo lido do arquivo "stdin", que neste caso é a entrada do usuário no terminal.
*/
var valores = input.split("\n"); //é definido o parametro de separação
var A = parseInt(valores.shift());
var B = parseInt(valores.shift());
/* 
    valores.shift(): O método shift() é uma função de array em JavaScript que remove o primeiro elemento do array e retorna esse elemento. O array é modificado após a chamada do shift(), com todos os outros elementos movendo-se para um índice inferior. Neste caso, valores.shift() remove o primeiro elemento do array valores.
    parseInt(valores.shift()): A função parseInt() é usada para analisar uma string e retornar um inteiro na base especificada. Aqui, estamos passando o resultado de valores.shift() para parseInt(). Isso significa que estamos convertendo o primeiro elemento removido de valores (que é uma string) em um número inteiro.
    var A = ...: Estamos atribuindo o resultado da conversão para um número inteiro à variável A. Isso significa que A conterá o valor do primeiro elemento de valores convertido em um número inteiro.
*/
var X = A+B;

console.log("X = " + X);