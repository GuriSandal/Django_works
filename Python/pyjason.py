import json

student = {
    'name' : 'Gurjant',
    'r_no':1,
    'subjects' : ['Python', 'Django'],
    'hobbies' : ('sleeping', 'codning'),
    'is_present' : True,
    'is_absent' : False,
    'singing' : None,
}

# print(type(student))
# print(student)

to_json = json.dumps(student, indent=4)
print(type(to_json))
print(to_json)


to_py = json.loads(to_json)
print(type(to_py))
print(to_py)