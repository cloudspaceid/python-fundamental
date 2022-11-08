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