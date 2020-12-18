import json
friends = {'dan': [20, 'London', 223432], 'Maria': [25, 'Madrid', 423789]}

with open('friends.json', 'w') as f:
    json.dump(friends, f, indent=4)

json_string = json.dumps(friends, indent=4)
print(json_string)