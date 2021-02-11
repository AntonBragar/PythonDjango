array = ['sun', 'moon', 'star', 'star', 'star', 'moon', 'sun', 'star', 'moon', 'sun']

for elem in array:
    if 'star' in array:
        array.remove('star')
    if 'moon' in array:
        array.remove('moon')

print(array)