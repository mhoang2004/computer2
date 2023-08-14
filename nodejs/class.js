// `this` keyword is used inside of a class and refers to the current instance. No more, no less.

class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }

    intro() {
        console.log("My name is " + this.name + ". I'm " + this.age)
    }
}

const PI = 3.14

class Student extends Person {
    constructor(name, age, univer, className) {
        super(name, age)
        this.PI = 3.14
        this.univer = univer
        this.className = className
    }

    say_hi() {
        this.words = "Hello lmao"
        console.log(this.words);
    }

}

class Doctor extends Person {
    constructor(name, age, job, salary) {
        super(name, age)
        this.job = job
        this.salary = salary
    }
}

class Teacher extends Person {
    constructor(name, age) {
        super(name, age)
    }
}

class MathTeacher extends Teacher {
    constructor(name, age, subject) {
        super(name, age)
        this.subject = 'math'
    }
}

const per1 = new Person("Hoang", 19)
per1.intro()

const stu1 = new Student("Liu", 12, "Cambodia", "IT")

stu1.say_hi()

console.log(stu1.words)