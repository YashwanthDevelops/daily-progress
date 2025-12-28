# import json 

# people_string = ''' 
# {
#     "people" : [
#     {
#         "name" : "Yashwanth",
#         "phone" : "123456789",
#         "emails" : ["temp@mail.com", "temp2@mail.com"],
#         "has_license" : false
#     },
#     {
#         "name" : "John Doe",
#         "phone" : "98765432",
#         "emails" : null,
#         "has_license" : true
        
#     }
#     ]
# }'''

# data = json.loads(people_string)

# # for person in data["people"]:
# #     print(person['name'])

# for person in data["people"]:
#     del person["phone"]

# new_string = json.dumps(data, indent = 2,sort_keys=True)
# print(new_string)

import json

with open("/home/yashwanth/projects/daily-progress/notes/python/17.1.JsonFile.json", 'r') as jsonFile:
    data = json.load(jsonFile)

# for state in data['states']:
#     print(state['name'],state['addreviation'])

for state in data['states']:
    del state['abbreviation']

with open ('17.02.json', 'w') as jsonFile:
    json.dump(data, jsonFile, indent = 4)