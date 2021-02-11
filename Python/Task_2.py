def startWith_A(word):
    return word[0] == "A"


fruit = ['Apricot', 'Ananas', 'Grape', 'Cherry', 'Orange', 'Apple']
filtered_object = filter(startWith_A, fruit)

print(list(filtered_object))
