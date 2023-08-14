# be serious with JSON

import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "title": ["engineer", "programmer"]
}

#? convert to json
personJSON = json.dumps(person, indent = 4)
# print(personJSON)

with open("person.json", "w") as file:
    #? dump into a file
    json.dump(person, file)

#? decode a JSON
# with open("person.json", "r") as file:
#     new_person = json.load(file)
# print(new_person["name"])

#? Passing a Class in JSON
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Max", 12)

def encode_user(o): #o -> object
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type is not JSON serializable")
    
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

#learn udemy, finish how node works

a = {'a': 1, 'b': 2}

        

