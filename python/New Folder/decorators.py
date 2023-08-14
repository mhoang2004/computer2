import functools

# 2 different decorators: fuction decorators and class decorators

#! decorator: take another function as argument and extends the function
#? => allows you to add new functionality to an existing function

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")
    
    return wrapper

#===
@start_end_decorator
def add5(x):
    return x + 5
# add5(10)
#========
#* the same with
# start_end_decorator(add5)(10)
#===

#* but problem is python will cofuse the fuction name
# print(add5.__name__)

#* to fix it: | import functools | and use `@functools.wraps(func)` before wrapper function


#|||||||||||||||||||||-BIG EXAMPLE-||||||||||||||||||
def repeat(num_times):
    def decorators_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                res = func(*args, **kwargs)
            return res
        return wrapper
    return decorators_repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

# equivalent to 
#? greet = repeat(num_times=4)(greet)

@start_end_decorator
@repeat(num_times=4)
def bye(name):
    print(f"Bye {name}")
# bye("Tom")

############Class decorator#############
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls # count how many times func is called
def say_sorry(name):
    print(f"Hello {name}")

say_sorry("Ken")
say_sorry("Ken")
say_sorry("Ken")


            



