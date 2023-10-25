#python dictionary
users = {
    'id' : 2,
    'name' : 'John',
    'username' : 'john',
    'email' : 'john@mail.com ',
    'address': {
        'street': 'Pemuda',
        'city': 'Semarang',
        'Province': 'Jawa Tengah'
    }
}
print(users)
print(users['name'])

print(users['address'])
print(users['address']['street'])

print(type(users))

print('\nUbah dictionary ke json')
import json
result = json.dumps(users)
print(result)
print(type(result))

#export json to file
with open('../result.json', 'w') as file:
    json.dump(users, file)