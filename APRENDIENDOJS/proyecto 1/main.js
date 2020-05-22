//console.log({"username": "ryan"});





var nombre = "Jon"; //variables

let apellido = "carter"

nombre = 'Pepe'; // Reasignacion de Variables

console.log(nombre)

const PI = 3.1415;

const id = 'user 01'
//camelcase
let nombreDePersona = 'gordon'

//operadores (+,-,*,/)

let numeroUno = 60;
let numeroDos = 100;

let resultado= numeroUno + numeroDos;

console.log(resultado)

// Concatenacion de strings
let name = 'John'
let surname = 'Carther'

let complete = name + ' ' + surname;

console.log(complete)

// Operadores de comparacion(<,>,==,!=,<=,>=)
let numberOne = 100;
let numnerTwo = 500;

let result = numberOne > numnerTwo

console.log(result)

let passwordDB = 'pepe123'

let input = 'pepe123'

let final = passwordDB == input

//Condicionales
if (final === true) {
    console.log('Login correcto')

} else{
    console.log('Contrseña Incorrecta')
}


let score = 70

if (score > 30) {
    console.log('Necesitas practicar mas')
} else if (score > 15) {
    console.log('Estas mejorando')
}
else {
    console.log('Debes de seguir el tutorial')
}

let typeCard = 'fklldkv'

switch(typeCard) {
    case 'Debid Card':
        console.log('Esta es una tarjeta de debito');
        break;
    case 'Credit Card':
        console.log('Esta es una tarjeta de credito');
        break;
    default:
        console.log('No card')
}

//bucles
/*let count = 49;

while(count >= 0) {
    console.log(count);
    count--;
}*/

//arrays con bucles
let names = ['ryan', 'Joe', 'John', 'Mario'];

for(let i = 0; i < names.length; i++ ) {
    console.log(names[i]);
}

function saludar(no) {
    console.log(no)
    console.log('Hello')
}

saludar('Marcus');


/* tipos de datos

"Hello world" // string
'hello world'//string


//boleano
true
false


arrays

['Jou', 'Ryan', 'Marta']
[1, 2, 3]
[true, false, true, false]

//objeto
'ryan'
70,4
14
true


{
    "username": 'ryan', //Clave,
    "score": 70.4,
    "hours": 14,
    "professional": true,
}

// claves como si fueran strings*/



