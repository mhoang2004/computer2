import random

#? float random [0, 1)
print(random.random())

#? float random [a, b)
print(random.uniform(1, 10))

#? int random [a, b]
print(random.randint(1, 10))

#? take 3 elements of a list
my_list = list("AJJSNCKLSJ")
a = random.sample(my_list, 3)
print(a)

#? shuffle
random.shuffle(my_list)
print(my_list)

#? reproduce with seed
random.seed(1)
print(random.random())
random.seed(1)
print(random.random())


