const { log } = require('console')
const fs = require('fs')
const superagent = require('superagent')

fs.readFile(`${__dirname}/dog.txt`, (err, data) => {
    log(`Breed: ${data}`)

    superagent
        //  get method return a promise (not data) as soon as we sending a request
        // => promise doesn't have value yet because the server is still getting the data asynchronously in the background
        // => server promising us that it will get some data back in the future
        .get(`https://dog.ceo/api/breed/${data}/images/random`)
        // when the promise is done the call back function in then method will be called
        .then((res) => {
            // res have res.header and res.body
            log(res.body.message)

            fs.writeFile('dog-img.txt', res.body.message, (err) => {
                log('Random dog image saved to file!')
            })
        })
        // beginning it's a pending promise and when it successfully gets the data => a resolved promise
        // a resolved promise might not always be successful, may be have an error
        // => we use `catch` method if it there was an error
        .catch((err) => log(err.message))
})

/*

*/
