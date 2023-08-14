

//? require function returns `exports` of the required module

// module.exports

//IIFE stand for Immediately Invoked Function Expression,

/*
    ? use module.exports to export one single varialbe
    * -> module.exports = Calculator
    
    
    ? use exports to export multiple variables
    * => exports.add = (a, b) => a + b
    * => exports.multiple = (a, b) => a * b
    * 
 */

/*
    ! we are in a function
    console.log(arguments) #return all arguments
*/




// an array contain all value parsed into a function
//! all code we write here attually wrapped into a function
//console.log(arguments); 

//console.log(require("module").wrapper);

// how to write Class in ES6

// import we can call it something else when save a result to funtion
// classes we use upper case names
//? import once (module.exports)
const C = require('./test-module-1')

const cal1 = new C //?

//console.log(cal1.add(5, 4));


//? import multiple (exports)
const cal2 = require('./test-module-2') // or
const {add, sub, mul, divide} = require('./test-module-2')

// console.log(cal2.add(2, 2));
// console.log(divide(4, 2));
//? Caching
require('./text-module-3')() // only this will run full file
require('./text-module-3')()
require('./text-module-3')()
require('./text-module-3')()