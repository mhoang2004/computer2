class Calculator {
    add(a, b) {
        return a + b
    }

    sub(a, b) {
        return a - b
    }

    mul(a, b) {
        return a * b
    }

    divide(a, b) {
        return a / b
    }
}

// we want to export one single value
module.exports = Calculator

//* same with 

// module.exports = class {
//     add(a, b) {
//         return a + b
//     }

//     sub(a, b) {
//         return a - b
//     }

//     mul(a, b) {
//         return a * b
//     }

//     divide(a, b) {
//         return a / b
//     }
// }
