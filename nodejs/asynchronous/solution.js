fs = require('fs')
const { log } = require('console')
const superagent = require('superagent')

// `readFilePro` return a promise
// it take a file name as arg
const readFilePro = (file) =>
    new Promise((resolve, reject) => {
        fs.readFile(file, (err, data) => {
            if (err) {
                //what we pass here will be pass to the arg of .catch function
                reject('I could not find that find 🤔')
            }
            //what we pass here will be pass to the arg of .then function
            resolve(data)
        })
    })

const writeFilePro = (file, data) => {
    return new Promise((resolve, reject) => {
        fs.writeFile(file, data, (err) => {
            if (err) reject('Can not write to file')
            resolve('success') //something like return data if successful
        })
    })
}

// readFilePro(`${__dirname}/dog.txt`)
//     .then((data) => {
//         log(`Breed: ${data}`) //data is the content in dog.txt (retriever)
//         return superagent.get(`https://dog.ceo/api/breed/${data}/images/random`) //return a promise
//     })
//     .then((res) => {
//         log(res.body.message)
//         return writeFilePro('dog-img.txt', res.body.message)
//     })
//     .then(() => {
//         log('Random dog image saved to file!')
//     })
//     .catch((err) => log(err))

//*================!!!!===================
//! async/await

/* - `async` keyword simply mean this is a special function that is asynchronous 
   - this function keeps running in the background while performing the code in it
   - return a promise */
const getDogPic = async () => {
    try {
        // wait until promise done and store to the data variable
        // wait for load data in dog.txt file  // return a promise
        const data = await readFilePro(`${__dirname}/dog.txt`)
        log(`Breed: ${data}`)

        // wait for load img in the internet //return a promise
        // const res = await superagent.get(`https://dog.ceo/api/breed/${data}/images/random`)

        const res1Pro = superagent.get(`https://dog.ceo/api/breed/${data}/images/random`)
        const res2Pro = superagent.get(`https://dog.ceo/api/breed/${data}/images/random`)
        const res3Pro = superagent.get(`https://dog.ceo/api/breed/${data}/images/random`)

        //request three promise at the same time!!
        const allPros = await Promise.all([res1Pro, res2Pro, res3Pro])

        const imgs = allPros.map((el) => el.body.message)

        //wait for write res in dog-img.txt
        await writeFilePro('dog-img.txt', imgs.join('\n'))
        log('Random dog image saved to file!')
    } catch (err) {
        log(err)

        // the async will always success
        // thorw an err will marked it fail
        throw err
    }
    return 'doing...'
}

/*
    log('before')
    
    // !run in the background to not to block the event loop/ main thread
    getDogPic().then((x) => {
        log(x)
    })
    log('after')

 */

;(async () => {
    try {
        log('before')
        // getDogPic is a async func, so it return a promise but the value of promise is what asyns func return!
        const x = await getDogPic()
        log(x)
        log('after')
    } catch (err) {
        log(err)
    }
})()

// most important thing is async funtion automatically //!return a promise
