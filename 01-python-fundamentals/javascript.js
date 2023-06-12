// Variables
let myVar = 1  // we use camel case in JS
const myConstant = "don't change me!"

// Functions
function myFunc(param1, param2) {
    // do something
}

// Simple data types
let myInt = 0
let myFloat = 3.14
let myBool = true
let myString = "hello"  // or 'hello'
let myArray = [1, 2, 3, 4]
let myObject = {name: 'joe', age: 21}
let myUndefined = undefined
let myNull = null

// Type checking
typeof myInt

// Type converstion
parseInt('1')
parseFloat('3.14')
String(1234)
Boolean(99)


// Printing
console.log('print me!')

// Arrays/Lists
let arrayAbc = ['a', 'b', 'c']
arrayAbc[0]  // => 'a'
arrayAbc[0] = 'z'  // ['z', 'b', 'c']
arrayAbc.length  // => 3
arrayAbc.push('d')  // ['z', 'b', 'c', 'd']

// JSON Objects/Dictionaries
let myJsonObj = {
    name: "joe",
    age: 44
}
myJsonObj['newkey'] = 'new value'
myJsonObj['badkey']  // => undefined

// Conditionals
if (true) {
    // do something
} else if (false) {
    // do something else
} else {
    // catch-all
}

// Comparison Operators
10 < 15   // less than => true
10 > 15   // greater than => false
4 <= 4    // less than/equal => true
4 >= 5    // greather than/equal => false
12 === 12 // equal => true
12 !== 12 // no equal => false

// Logical Operators
true && true  // AND => true
true || false // OR => true
!true         // NOT => false

// while loop
while (false) {
    // loop code
}

// for loop
for (let i = 0; i < 10; i++) {
    // loop code
}

// for item in collection
let seq = ['a', 'b', 'c']
for (let char of seq) {
    // loop code
}