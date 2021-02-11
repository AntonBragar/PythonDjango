# car_prices = {
#     'Audi': 2000,
#     'BMW': 2700,
#     'Opel': 1300,
# }
#
# car_prices['Mazda'] = 4000
#
# del car_prices['Opel']
# print(car_prices)

person = {
    'first name': 'Anton',
    'last name': 'Brahar',
    'age': 24,
    'hobbies': ['gaming', 'travelling', 'boxing'],
    'children': {
        'son': 'Semen',
        'daughter': 'Victoria'
    }
}

print(person['age'])
print(person['hobbies'])
print(person['children']['daughter'])

person['car'] = 'Mazda'
print(person)

person['children']['son_2'] = 'Arseniy'
print(person)